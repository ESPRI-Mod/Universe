from abc import ABC, abstractmethod
from typing import Union
from fastapi import FastAPI
from importlib import import_module
import inspect
# from poc_repo_api.code._generated.institution import Institution
# from poc_repo_api.code._generated.forcing_index import ForcingIndex
# from poc_repo_api.code._generated.realization_index import RealizationIndex
# from poc_repo_api.code._generated.initialization_index import InitializationIndex
# from poc_repo_api.code._generated.physic_index import PhysicIndex 
# from poc_repo_api.code._generated.variant_label import VariantLabel
import re
from pathlib import Path

import logging
import sys
from poc_repo_api import repo_path
import json

import collections.abc

from sparql_endpoint import sparql_router
from uri_server import uri_router
app = FastAPI()
app.include_router(sparql_router)
app.include_router(uri_router)
#print("TOTO")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter("%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s")
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)
#
# def getinstitutionDict():
#     institution_path = repo_path / "/repos/Universe/Institution")
#     res = {}
#     for filepath in institution_path.glob("*.json"):
#         institut = Institution.model_validate_json(filepath.read_text())
#         #logger.info(a)
#         res[institut.id]=institut
#         #logger.info(res)
#     return res
#
# def getRegexDict():
#     regex_path = repo_path / "/repos/Universe/Regex"
#     res={}
#     for filepath in regex_path.glob("*.json"):
#         print(filepath)
#         rege = Regex.model_validate_json(filepath.read_text())
#         res[rege.id]=rege
#     return res
#
# def getCompositeDict():
#     regex_path = repo_path / "/repos/Universe/Composite"
#     res={}
#     for filepath in regex_path.glob("*.json"):
#         print(filepath)
#         composite = Composite.model_validate_json(filepath.read_text())
#         res[composite.id]=composite
#     return res
#

def update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update(d.get(k, {}), v)
        else:
            d[k] = v
    return d
def get_classes_from_module(module):
    # Use inspect.getmembers to get all classes defined in the module
    classes = inspect.getmembers(module, inspect.isclass)
    # Filter out classes that are not defined in this module
    module_classes = {name: cls for name, cls in classes if cls.__module__ == module.__name__}
    return module_classes

def getCMIP6PlusDict():
    CMIP6Plus_path = repo_path / "repos/CMIP6Plus_CV"
    res={}
    for filepath in CMIP6Plus_path.glob("*.json"):
        print(filepath)
        # Where are the object definiton ? 
        # look for base :
        CV_file = json.loads(filepath.read_text())
        #print(CV_file)
        #file_paths = CV_file["@context"]["@base"]
        for short_term in CV_file["@graph"]:
            #print(short_term)
            if short_term["@id"] in insts.keys(): # only institutoin !!! => need to check either type or directory name to know witch pydantic to use
                res[short_term["@id"]] = insts[short_term["@id"]]
            # need probably 1 added key like res["data-descriptor"]["id"] = pydantic instance btu same philo could be applied
                #print(res[short_term["@id"]] )
                res[short_term["@id"]] =Institution.parse_obj(update(res[short_term["@id"]].dict() ,short_term))


    return res


def getUniverseDict():
    Universe_path = repo_path / "repos/Universe"
    res ={}
    for dir_path in Universe_path.iterdir():
        res[dir_path.stem]={}
        for file_path in dir_path.glob("**/*.json"):
             #print("TEST to read : ", file_path)
            
            try:
                json_data_str = Path(file_path).read_text()

                #print(dir_path.name)
                #models_path = dir_path / "models" 
                #pymodel_path = models_path / f"{dir_path.stem}.py"
                #breakpoint()
                #print("TRY TO IMPORT:",pymodel_path)
                module_name = f"poc_repo_api.repos.Universe.{dir_path.stem}.models.{dir_path.stem}"
                module = import_module(module_name)
                clss = get_classes_from_module(module)
                #breakpoint()
                globals().update(clss)

                py_instance= None
                for class_name in clss.keys():

                    if class_name =="ConfiguredBaseModel" :
                        continue
                    try:
                        pymodel = getattr(module, class_name)

                        py_instance = pymodel.model_validate_json(json_data_str)

                        #breakpoint()
                    except Exception as e: 
                        #print("NON")
                        continue

                #print(f"#########{dir_path.stem}#################")

                #print(py_instance)
                #print("##########################")

                #print(clss.keys())
                #print("OK")
                #breakpoint()
                #pymodel = getattr(test, dir_path.stem)
                #print("BLA")
                #breakpoint()
                #pymodel = globals()[''.join(word.capitalize() for word in dir_path.name.split("_"))]
                #print(pymodel)
                #print(Path(file_path).read_text())
                #print(dir_path.stem)
                #print(file_path.stem)
                res[dir_path.stem][file_path.stem]=py_instance
                
                #json_data_str = Path(file_path).read_text()
                #res[dir_path.stem][file_path.stem]= pymodel.model_validate_json(json_data_str)
                #print("OK")

            except Exception as e:
                print("e:",e)
            #Composite.model_validate_json(file_path.read_text())
            #res[dir_path.name][file_path.stem]=
    return res


universe= getUniverseDict()
print(universe)

# insts = getinstitutionDict()
# regs = getRegexDict()
# composites = getCompositeDict()
#cmip6plus = getCMIP6PlusDict()
#print(cmip6plus)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/institution", response_model=list[Institution])
def getinstitutions():
    #logger.info("toto")
    return [v for k,v in universe["institution"].items()]

@app.get("/institution/{institution:str}", response_model=Institution)
def read_insts(institution_id: str):
    #insts = getinstitutionDict()
    #logger.info(insts)
    return universe["institution"][str(institution_id)]

# @app.get("/regex", response_model=list[Regex])
# def getrealizations():
#     #logger.info("toto")
#     return [v for k,v in regs.items()]

# @app.get("/regexs/{regex:str}", response_model=Regex)
# def read_reg(regex_id: str):
#     #insts = getinstitutionDict()
#     #logger.info(insts)
#     return regs[str(regex_id)]
#
# @app.get("/composite", response_model=list[Composite])
# def getcomposites():
#     #logger.info("toto")
#     return [v for k,v in composites.items()]
#
#
#
# @app.get("/composites/{composite:str}", response_model=Composite)
# def read_composite(composite_id: str):
#     #insts = getinstitutionDict()
#     #logger.info(insts)
#     return composites[str(composite_id)]
#
#isvalid try to validate expression trgrouht terms, regex, posite ??
class Validation(ABC):
    @abstractmethod
    def is_valid(self,term,dd_id,instance):
        pass

class Method():
    def __init__(self,validation:Validation):
        self.validation = validation
    def is_valid(self,term,dd_id,instance):
        return self.validation.is_valid(term,dd_id,instance)


class RegexValidation(Validation):
    def is_valid(self,term,dd_id,instance):
        if re.compile(instance.regex).match(term) is not None:
            return f"could be valid as {dd_id} with term : {instance.id}"
        return ""

class ListValidation(Validation):
    def is_valid(self,term,dd_id,instance):
        print(term, instance.id)
        if term == instance.id:
            return f"could be valid as {dd_id} with term : {instance.id}"
        return ""

def get_pydantic_instance_from_id(id):
    for dd_id,dd in universe.items():
        for k,v in dd.items():
            #print(k,v )
            if v.id==id:
                #print("TROUVEEEEEEEEEEE",v)
                return v

class CompositeValidation(Validation):
    def is_valid(self,term,dd_id,instance):
        print("COMPOSITE")
        res = {}
        res["Valid"]=[]
        # if instance.separator!="":
        #     term_parts = term.split(instance.separator)
        # else:
        deduced_terms= []
        remain_term = term
            
        for part in instance.parts:
            print("Déja on va essayer de trouver")
            print(part)
            model_instance = get_pydantic_instance_from_id(part.id)
            if model_instance == None:
                print("on connait pas cette id : ",part.id)
                return
            #print(model_instance)

            if model_instance.validation_method == "list":
                method = Method(ListValidation())

            if model_instance.validation_method=="regex":
                method = Method(RegexValidation())

            if model_instance.validation_method=="composite":
                method = Method(CompositeValidation())



            for i in range(1,len(remain_term)+1):
                temp = method.is_valid(remain_term[:i],part,model_instance)
                if temp != "":
                    # pour cette part on a trouvé la parti qui correspond
                    
                    print("ON PASSE PAR LA", remain_term[:i])
                    res["Valid"].append(temp)
                    deduced_terms.append(remain_term[:i])
                    remain_term=remain_term[i:]
                    continue
        print(res)
        return res
#               part_term = remain_term[:i]





@app.get("/isvalidterm/{term:str}") #TODO regex/composite/list
def is_term_valid(term:str):
    res = {} 
    res["Valid"]=[]

    for dd_id,dd in universe.items():
        for k,v in dd.items(): 

            #print(v)
            #print(v.validation_method)
            if v.validation_method == "list":
                method = Method(ListValidation())

            if v.validation_method=="regex":
                method = Method(RegexValidation())

            if v.validation_method=="composite":
                method = Method(CompositeValidation())
            


            temp = method.is_valid(term,dd_id,v)
            if temp != "":
                res["Valid"].append(temp)

    if len(res["Valid"])==0:
        return {"Valid" : "false" }
    return res

# @app.get("/isvalidregex/{regex-descriptor}/{term:str}")
# def is_valid_regex(regex_descriptor_id:str,term:str):
#     if regex_descriptor_id in list(regs.keys()):
#         if re.compile(regs[regex_descriptor_id].regex).match(term) is not None:
#             return {"valid": "True"}
#         else:
#             return {"valid":"False"}
#     else:
#         return {"valid": "Maybe but we regex-descriptor is NOT known"}
#
# @app.get("/isvalidcomposite/{composite-descriptor}/{term:str}")
# def is_valid_composite(composite_descriptor_id:str,term:str):
#     if composite_descriptor_id in list(composites.keys()):
#         if composites[composite_descriptor_id].separator =="":
#             deduced_terms= []
#             
#             remain_term = term
#             for part in composites[composite_descriptor_id].parts:
#                 # part is an instance of DataDescriptorId <= change his name ? 
#                 if part.id in insts.keys(): # ONLY insitution !!!
#                     pass ## NOT implemented
#                 if part.id in regs.keys():
#                     
#                     for i in range(1,len(remain_term)+1):
#                         part_term = remain_term[:i]
#
#                         if re.compile(regs[part.id].regex).match(part_term) is not None:
#                             remain_term = remain_term[i:]
#                             break
#                         if i == len(remain_term):
#                             return {"valid":"False"}
#
#             return {"valid":"True"}
#         else:    
#             deduced_terms = term.split(composites[composite_descriptor_id].separator)
#     else:
#         return {"valid": "Maybe but we composite-descriptor is NOT known"}


@app.get("/isvalidterm/{project:str}/{descriptor:str}/{term:str}")
def is_valid_for_project(project:str,descriptor:str,term:str):
    if project == "CMIP6Plus":
        if term in list(cmip6plus.keys()):
            return {"valid":"true"}
        else:
            return {"valid":"false"}
    else:
        return {"valid" : "NO, this project is not known by this API"}

@app.get("/term/{project:str}/{descriptor:str}")
def terms_for_project(project:str,descriptor:str):
    if project == "CMIP6Plus":
        if descriptor == "institution":
            return [v for k,v in cmip6plus.items()]
        else:
            return {"msg":"dont know this term"}
    else:
        return {"msg" : "NO, this project is not known by this API"}


