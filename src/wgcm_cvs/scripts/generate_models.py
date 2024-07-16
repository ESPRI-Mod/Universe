import json
from pathlib import Path
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.generators.pydanticgen import PydanticGenerator


schemas_path = Path("schemas")
out_base_dir = Path("../..")
print( "######## GENERATION Pydantic models from LinkML #######")


for file_path in schemas_path.glob("*.yaml"):
    
    print(file_path)
    DD_path = out_base_dir / file_path.stem / Path("models")
    DD_path.mkdir(parents=True,exist_ok=True)
     
    pydanticgen = PydanticGenerator(file_path, extra_fields="allow")
    
    with open(DD_path / f"{file_path.stem}.py", "w") as f:
         f.write(pydanticgen.serialize())


print( "######## GENERATION JSON models from LinkML #######")


for file_path in schemas_path.glob("*.yaml"):
    
    print(file_path)
    DD_path = out_base_dir / file_path.stem / Path("models")
    DD_path.mkdir(parents=True,exist_ok=True)
     
    jsongen = JsonSchemaGenerator(file_path)
    
    with open(DD_path / f"{file_path.stem}.json", "w") as f:
         f.write(jsongen.serialize())

print("END schemas generation")
