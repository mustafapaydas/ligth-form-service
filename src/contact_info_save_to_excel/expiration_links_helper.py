import os
from .json_file_helper import *
import datetime

def expired_links():
    for i in os.listdir("jsons"):
        if (i.strip(i[:-4]) == "json"):
            info = read_json_file(i.strip(i[-5:]))
            startingTime=os.stat(f"jsons/{i}").st_ctime

            generateDate=datetime.datetime.fromtimestamp(startingTime)
            now=datetime.datetime.now()
            validityTime=int(info["validityTime"])
            validityTime=datetime.timedelta(hours=validityTime)

            if (generateDate+validityTime) < now:
                os.remove(f"jsons/{i}")