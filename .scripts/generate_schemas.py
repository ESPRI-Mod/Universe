from pathlib import Path
from poc_repo_api import repo_path
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.generators.pydanticgen import PydanticGenerator
from linkml.generators.jsonldcontextgen import ContextGenerator
from linkml.generators.jsonldgen import JSONLDGenerator
#
# schInstitutionPath = Path("linkml_schemas/institution.yaml")
# institutionJsonSchemasRepoPath = Path("../repos/Universe/Institution/Schemas/institution.json")
#
# print("BEGIN schemas generation")
# print("jsonschema generation ...")
# jsongen = JsonSchemaGenerator(schInstitutionPath)
# strjson = jsongen.serialize()
# with open(institutionJsonSchemasRepoPath, "w") as f:
#     f.write(strjson)
# with open("_generated/institution.json", "w") as f:
#     f.write(strjson)
#
# print("pydantic schema generation ...")
# pydanticgen = PydanticGenerator(schInstitutionPath, extra_fields="allow")
# strpydan = pydanticgen.serialize()
# with open("_generated/institution.py", "w") as f:
#     f.write(strpydan)
#     
#
# print("jsonld schema context generation ...")
# jsonldcontextgen = ContextGenerator(schInstitutionPath)
# strcontext = jsonldcontextgen.serialize()
# with open("_generated/institution.context.jsonld","w") as f:
#     f.write(strcontext)
#
# jsonldgen = JSONLDGenerator(schInstitutionPath)
# strjsonld = jsonldgen.serialize()
# with open("_generated/institution.context.jsonld","w") as f:
#     f.write(strjsonld)
#

schemas_path = repo_path / "code/linkml_schemas/"

print( "######## GENERATION Pydantic models from LinkML #######")

universe_path = repo_path / "repos/Universe/"

for file_path in schemas_path.glob("*.yaml"):
    print(file_path)
    print(file_path.stem)
    
    DD_path = universe_path / file_path.stem / Path("models")
    DD_path.mkdir(parents=True,exist_ok=True)
    #breakpoint()
     
    pydanticgen = PydanticGenerator(file_path, extra_fields="allow")
    #print("COUCOU", pydanticgen)
    with open(f"_generated/{file_path.stem}.py", "w") as f:
         f.write(pydanticgen.serialize())

    #print("COUCOU")

    with open(DD_path / f"{file_path.stem}.py", "w") as f:
         f.write(pydanticgen.serialize())



#
# print( "######## GENERATION json-ld context from LinkML #######")
#
# for file_path in schemas_path.glob("*.yaml"):
#     print(file_path)
#     print(file_path.stem)
#     json_context_gen = ContextGenerator(file_path)
#     with open (f"_generated/contexts/{file_path.stem}.jsonld","w") as f:
#         f.write(json_context_gen.serialize("http://127.0.0.1/uri/"))

print("END schemas generation")
