import json
import os

def readJsonFile(email):

    with open(f"Jsons/{email}.json","r") as file:
        info = json.load(file)
    return info

def writeJsonFile(email,jsonString):
    with open(f"Jsons/{email}.json","w") as file:
        json.dump(jsonString,file)

