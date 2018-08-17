import requests as request

def getHeaders(url):
    res = request.get(url)
    if res.status_code == 200:
        print(res.headers)
        print(res.headers['Date'])
    else:
        print(f"Error Code: {res.status_code}")


getHeaders('https://www.google.com')
