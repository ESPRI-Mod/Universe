
from pathlib import Path
from linkml.generators.common.type_designators import SchemaView
from linkml.generators.jsonldcontextgen import ContextGenerator
from linkml.generators.jsonldgen import JSONLDGenerator
from linkml_runtime.dumpers import JSONDumper
from linkml_runtime.loaders import JSONLoader
from linkml_runtime.linkml_model.meta import SchemaDefinition
import yaml
from linkml.generators.pythongen import PythonGenerator
import json
from poc_repo_api import repo_path

schemas_path = repo_path / "code/linkml_schemas"

universe_path = repo_path / "repos/Universe"

print( "######## GENERATION json-ld with context from LinkML #######")

# for file_path in universe_path.glob("institution/**/*.json"):
#     sch_file = Path(str(schemas_path) + "/" + file_path.parent.parent.stem +".yaml")
#
#     json_context_gen = ContextGenerator(sch_file)
#     base = "http://127.0.0.1:8000/uri/"
#     #base = "http://toto"
#     str_context = json_context_gen.serialize(base)
#     #breakpoint()
#     jsonld_context = json.loads(str_context)
#
#     jsonld_res = json.loads(file_path.read_text())
#     jsonld_res["@context"]=jsonld_context
#     
#     with open (f"_generated/institutions/{file_path.stem}.jsonld","w") as f:
#         json.dump(jsonld_res, f, indent = 2)
#
#
#GENERALIZATION
for file_path in universe_path.glob("**/terms/*.json"):
    sch_file = Path(str(schemas_path) + "/" + file_path.parent.parent.stem +".yaml")

    json_context_gen = ContextGenerator(sch_file)
    base = f"http://127.0.0.1:8000/uri/"
    #base = "http://toto"
    str_context = json_context_gen.serialize(base)
    #breakpoint()
    jsonld_context = json.loads(str_context)

    jsonld_res = json.loads(file_path.read_text())
    jsonld_res["@context"]=jsonld_context

    Path(f"_generated/jsonld/{file_path.parent.parent.stem}").mkdir(parents=True,exist_ok=True)

    with open (f"_generated/jsonld/{file_path.parent.parent.stem}/{file_path.stem}.jsonld","w") as f:
        #print("ola",file_path.parent.parent.stem, file_path.stem)
        #print(jsonld_res)
        json.dump(jsonld_res, f, indent = 2)




    


    #
    #print(file_path)
    # print(file_path.parent.parent.stem, file_path.stem)
    # # on doit trouver le shema correspondant
    # print("schema file = ", str(schemas_path) + "/" + file_path.parent.parent.stem +".yaml")
    # sch_file = Path(str(schemas_path) + "/" + file_path.parent.parent.stem +".yaml")
    #
    #
    # with open(sch_file, 'r') as file:
    #     yaml_model = yaml.safe_load(file)
    # 
    # schema = SchemaDefinition(**yaml_model) 
    # sv = SchemaView(schema)
    # #breakpoint()
    #
    # target_class = "Institution"
    # python_module = PythonGenerator(schema).compile_module()
    # py_target_class = python_module.__dict__[target_class]
    # 
    # with open(file_path, 'r') as file:
    #     json_instance = file.read()
    #
    # breakpoint() 
    # loader = JSONLoader()
    #
    # instance = loader.load(source = file_path.read_text(),target_class=py_target_class)
    #
    # context = ContextGenerator(schema).serialize()
    # breakpoint()
    #
    #
    # dumper = JSONDumper()
    # json_ld = dumper.dumps(instance, contexts=context)
    # print(json_ld)
    #
    #
    # # json_ld_gen = JSONLDGenerator(sch_file,)
    # with open (f"_generated/institutions/{file_path.stem}.jsonld","w") as f:
    #     f.write(json_ld)


print("END file generation")
