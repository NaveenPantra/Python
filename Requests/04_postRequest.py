import requests as request


def postRequest(url, data=None):
    if data is None:
        print(f"Cannot post any data to the server")

    else:
        res = request.post(url, data=data)
        if res.status_code == 200:
            with open('./04_postRequest.html',"w") as file:
                file.write(res.text)
        else:
            print(f"Error code: {res.status_code}")


credentials = {
    f"uname": 'naveenpantra.np@gmail.com',
    f"pword": 'cr7naveen',
}
postRequest(f"https://project-wp-naveenpantra.c9users.io/", credentials)
