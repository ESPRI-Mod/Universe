from pathlib import Path
from poc_repo_api import repo_path
from rdflib import Graph




# the idea is to get all jsonld in a rdflib graph
 

def get_graph():
    jsonld_path = repo_path / "code/_generated/jsonld"
    g = Graph()

    for json_file in jsonld_path.glob("**/*.jsonld"):
        #print("toto",json_file)
        #if "index" in str(json_file):
        #    continue
        jsonld_str = json_file.read_text()
        #print(jsonld_str)
        #breakpoint()
        g.parse(data=jsonld_str,format='json-ld')
    return g
#g = Graph().parse(data=test_json, format='json-ld')
#for s,p,o in g.triples((None,None,None)):
#    print(s,p,o)
    
#print(list(g.triples((None,None,None))))
