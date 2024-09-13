import requests
import os
from requests.compat import importlib
import json


def get_github_files(owner, repo, directory):
    # GitHub API URL for repository contents
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{directory}"

    # Send GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        contents = response.json()
        
        # List to store file paths
        files = []

        # Loop through contents and get file paths
        for item in contents:
            if item['type'] == 'file':
                files.append(item['path'])
            elif item['type'] == 'dir':
                # If it's a directory, recursively fetch its contents
                files += get_github_files(owner, repo, item['path'])

        return files
    else:
        print(f"Failed to retrieve contents: {response.status_code}")
        return []

# Function to fetch and load JSON data from a URL
def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.json()


# Directory where the JSON files will be saved
save_dir = '../../data_descriptors/table/terms/'

fs = get_github_files("PCMDI","mip-cmor-tables","Tables")
fs = [fn.split("/")[-1] for fn in fs]
for filename in fs:

    if filename[:3]=="MIP":
        #print(filename)
        json_url = 'https://raw.githubusercontent.com/PCMDI/mip-cmor-tables/main/Tables/'+filename

        # Fetch the JSON data from both URLs
        data = fetch_json(json_url)

        name = data["Header"]["table_id"]

        vars = list(data["variable_entry"].keys())
        print(name, vars)
        
        term = {}
        term["id"] = name
        term["variable_entry"]=vars
        print(term)

        file_path = os.path.join(save_dir, f"{name}.json")
        with open(file_path, 'w') as f:
            json.dump(term, f, indent=4)
