import requests as request


def getRequest(url, params=None):
    # print(f"Getting request from: {url}?q={params['?q=']}")
    req = request.get(url, params)
    if req.status_code == 200:
        print(f"Got Response from: {req.url}")
        print(f"Encoding: {req.encoding}")
        req.encoding = f"ISO-8859-1"
        with open("02_gettingTheSearch.html", "w") as file:
            file.write(str(req.text))

    else:
        print(f"Cannot get the request...")


adder = f"https://www.google.com/search"
search = input("Enter the search term: ")
payload = {
    "q": search
}
getRequest(adder, payload)
