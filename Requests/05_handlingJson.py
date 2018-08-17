import requests as request
import simplejson as json


def getJsonData(url):
    res = request.get(url)
    if res.status_code == 200:
        with open("./05_fileJson.json", "w") as fiel:
            fiel.write(json.dumps(res.json()))
        print(f"{res.json()['coord']}")
    else:
        print(f"Error Code: {res.status_code}")


getJsonData(f"https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22")