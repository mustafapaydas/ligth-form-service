import os
from .JsonFileHelper import *
import datetime

def expiredLinks():
    for i in os.listdir("Jsons"):
        if (i.strip(i[:-4]) == "json"):
            info = readJsonFile(i.strip(i[-5:]))
            startingTime=os.stat(f"Jsons/{i}").st_ctime

            generateDate=datetime.datetime.fromtimestamp(startingTime)
            now=datetime.datetime.now()
            validityTime=info["validityTime"]
            validityTime=datetime.timedelta(hours=validityTime)

            if (generateDate+validityTime) < now:
                os.remove(f"Jsons/{i}")