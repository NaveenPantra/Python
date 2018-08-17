from bs4 import BeautifulSoup as BS
import requests as request


def getRequest(url, params):
    res = request.get(url, params)
    print(f"Requested url: {res.url}")
    if res.status_code == 200:
        soup = BS(res.text, "html5lib")
        doc = soup.prettify()
        with open("./01_start.html", "w") as file:
            file.write(res.text)


search = input("Enter the search string: ")
address = f"https://www.google.com/search"
payload = {
    'q': search
}

getRequest(address, payload)
