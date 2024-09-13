
import requests
import json
import os

# URLs of the JSON files on GitHub
json_url1 = 'https://raw.githubusercontent.com/PCMDI/mip-cmor-tables/main/MIP_grid_label.json'
# Directory where the JSON files will be saved
save_dir = '../../data_descriptors/grid/terms/'

# Create the directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

# Function to fetch and load JSON data from a URL
def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.json()

# Fetch the JSON data from both URLs
data1 = fetch_json(json_url1)

# Extract the activity_id dictionaries from both JSON files
source_ids1 = data1.get('grid_label', {})

#print(source_ids1)


for key, value in source_ids1.items():
    print(key)
    print(value)
    ## NEED TO MODIFIY 2,3 THINGS
    term ={}
    term["id"] = key
    term["label"] = key
    term["description"]=value
    
     
    file_path = os.path.join(save_dir, f"{key.lower()}.json")
    with open(file_path, 'w') as f:
        json.dump(term, f, indent=4)



