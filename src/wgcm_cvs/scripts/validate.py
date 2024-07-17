from pathlib import Path
import jsonschema
import json
from jsonschema.validators import validator_for
import importlib.util
import inspect


base_path = Path("../..")
dontlook = ["src","tests",".git",".venv","__pycache__",".pdm-build"]
for dir_path in base_path.iterdir():
    if dir_path.stem in dontlook or not dir_path.is_dir():
        continue

    print(dir_path)
    py_sch_name = dir_path.stem + ".py"
    json_sch_name = dir_path.stem + ".json"
    

    sch_path = dir_path / "models" / json_sch_name

    with open(sch_path,"r") as f :
        sch = json.load(f)

    cls = validator_for(sch)
    cls.check_schema(sch)
    validator = cls(sch)

    print("through jsonschema")


    rootdatapath = dir_path / "terms" 
    for path in rootdatapath.iterdir():
        if path.is_file():
            with open(path,"r") as fp:
                jsonstr = json.load(fp)

            print(validator.is_valid(jsonstr))
    

    print("through pydantic")
    for path in rootdatapath.iterdir():
        if path.is_file():
            class_name = "".join([part.capitalize() for part in dir_path.stem.split("_")])
            pydantic_module_file_path = dir_path / "models" / py_sch_name

            spec = importlib.util.spec_from_file_location(name=class_name, location=pydantic_module_file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            classes = inspect.getmembers(module,inspect.isclass)
            module_classes =  {name: cls for name, cls in classes if cls.__module__ == module.__name__}

            py_class = module_classes[class_name]
            
            #Institution.model_validate_json(path.read_text())
            py_instance = py_class.model_validate_json(path.read_text())
            print(py_instance)

print("END")
