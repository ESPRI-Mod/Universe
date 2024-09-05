import requests
import json
import os

# URLs of the JSON files on GitHub
json_url1 = 'https://raw.githubusercontent.com/WCRP-CMIP/CMIP6Plus_CVs/main/CMIP6Plus_source_id.json'

# Directory where the JSON files will be saved
save_dir = '../../data_descriptors/source/terms/'

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
source_ids1 = data1.get('source_id', {})

#print(source_ids1)


for key, value in source_ids1.items():
    print(key)
    print(value)
    ## NEED TO MODIFIY 2,3 THINGS
    value["id"] = value["label"]
    
    file_path = os.path.join(save_dir, f"{key.lower()}.json")
    with open(file_path, 'w') as f:
        json.dump(value, f, indent=4)



"""
# Create a dictionary with activity ID as key and a dictionary with long_name and url set to None
source_dict = {key: {'long_name': value, 'url': None} for key, value in source_ids1.items()}


# Save each activity as an individual JSON file
for key, value in source_dict.items():
    activity_data = {
        'id': key.lower(),
        'name': key,
        'cmip_acronym': key,
        'long_name': value['long_name'],
        'url': value['url']
    }
    file_path = os.path.join(save_dir, f"{key.lower()}.json")
    with open(file_path, 'w') as f:
        json.dump(activity_data, f, indent=4)

print("Activity files saved to", save_dir)
"""
