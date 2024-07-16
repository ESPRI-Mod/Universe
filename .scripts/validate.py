from pathlib import Path
import jsonschema
import json
from jsonschema.validators import validator_for
from poc_repo_api.code._generated.institution import Institution


print("BEGIN validate")
# 1/ get schema validator
schpath = Path("_generated/institution.json")

with open(schpath,"r") as f :
    sch = json.load(f)

cls = validator_for(sch)
cls.check_schema(sch)
validator = cls(sch)

# 2/ get each data and validate throufh jsonschema
print("through jsonschema")


rootdatapath = Path("../repos/Universe/Institution")
for path in rootdatapath.iterdir():
    if path.is_file():
        print(path)
        with open(path,"r") as fp:
            jsonstr = json.load(fp)

        print(validator.is_valid(jsonstr))


# Validate through pydantic => stricter and clearer

print("through pydantic")
rootdatapath = Path("../repos/Universe/Institution")
for path in rootdatapath.iterdir():
    if path.is_file():
        print(path)
        Institution.model_validate_json(path.read_text())

print("END")


