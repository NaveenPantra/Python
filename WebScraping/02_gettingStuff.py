from bs4 import BeautifulSoup as BS
import requests as request


def getStuff(url, params=None):
    res = request.get(url, params)
    print(f"The Requested URL: {res.url}")
    soup = BS(res.text, 'html5lib')
    if res.status_code == 200:
        links = soup.select('a')
        for link in links:
            print(link)
        print(f"Total links: {len(links)}")
    else:
        print(f"Error Code: {res.status_code}")


# address = "https://www.google.com/search"
# search = input("Enter Search String: ")
# payload = {
#     f"q": search,
# }
address = "https://project-wp-naveenpantra.c9users.io/"
# getStuff(address, payload)
getStuff(address)
