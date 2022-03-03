import json
import os

def read_json_file(email):

    with open(f"jsons/{email}.json","r") as file:
        info = json.load(file)
    return info

def write_json_file(email, jsonString):
    with open(f"jsons/{email}.json","w") as file:
        json.dump(jsonString,file)

