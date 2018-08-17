import requests as request


def getRequest(url):
    req = request.get(url)
    if req.status_code == 200:
        # print(f"{type(req.content)}")
        # print(f"{type(req.text)}")
        # print(f"{req.url}")
        with open("./01_requests.html", "w+") as file:
            file.write(req.text)


getRequest("https://www.google.co.in")
