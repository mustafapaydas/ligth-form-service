import json
import os
import file_helper
def read_json_file(email):

    with open(f"jsons/{email}.json","r") as file:
        info = json.load(file)
    return info

def write_json_file(email, jsonString):
    folder = "jsons"
    file_helper.exists_path(folder)
    with open(f"{folder}/{email}.json","w") as file:
        json.dump(jsonString,file)

