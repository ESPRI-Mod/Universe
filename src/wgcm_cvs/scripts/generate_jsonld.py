import json
from pathlib import Path
from linkml.generators.jsonldcontextgen import ContextGenerator
from rdflib import Graph

schemas_path = Path("schemas")
universe_base_path = Path("../..")
universe_path = Path("../../data_descriptors")
output_dir = Path("terms/jsonld")

base_base = "http://es-vocab.ipsl.fr/"

print( "######## GENERATION json-ld with context from LinkML #######")

# The idea is to generate jsonld ..
# the context is obtained from the linkml model
# the graph is obtain from de terms json file 

# the output could be
# for all known terms
# for one term only

# The output format could be 
# in jsonld file
# in rdflib graph

# PB : the linkml graph is in WGCM repo
# data is in WGCM_repo for the universe but elsewhere, i.e other repository for each project
# lets make it only for the universe for now




def generate_all_jsonld(gen_file=False)->list:
    res = []
    for sch_path in schemas_path.glob("*.yaml"):
        json_context_gen = ContextGenerator(sch_path)
        base = base_base + sch_path.stem + "/"
        str_context = json_context_gen.serialize(base)
        jsonld_context = json.loads(str_context)
        
        terms_path = universe_path / sch_path.stem / "terms" 
        for term_path in terms_path.glob("*.json"):
            jsonld_res = json.loads(term_path.read_text())
            jsonld_res["@context"] = jsonld_context
            res.append(jsonld_res)
            if gen_file:
                jsonld_dir = universe_path / sch_path.stem / output_dir
                jsonld_dir.mkdir(parents=True,exist_ok=True)
                file_name = term_path.stem + ".jsonld"

                with open (jsonld_dir / file_name,"w") as f:
                        #print("ola",file_path.parent.parent.stem, file_path.stem)
                        #print(jsonld_res)
                        json.dump(jsonld_res, f, indent = 2)

    return res

def generate_rdfgraph(jsonlds:list,filesave=False)->Graph:
    g=Graph()

    for jsonld in jsonlds:
        g.parse(data=jsonld,format='json-ld')

    if filesave : 
        g.serialize(destination= universe_base_path / "graph" / "es-vocab.ttl")
    return g



        # Path(f"_generated/jsonld/{file_path.parent.parent.stem}").mkdir(parents=True,exist_ok=True)
        #
        # with open (f"_generated/jsonld/{file_path.parent.parent.stem}/{file_path.stem}.jsonld","w") as f:
        #     #print("ola",file_path.parent.parent.stem, file_path.stem)
        #     #print(jsonld_res)
        #     json.dump(jsonld_res, f, indent = 2)

if __name__ == "__main__":

    jsonld_list = generate_all_jsonld(True)
    g = generate_rdfgraph(jsonld_list,True)
    print(g)
    for s,p,o in g.triples((None,None,None)):
        print(s,p,o)
  
