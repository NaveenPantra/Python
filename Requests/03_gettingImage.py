import requests as request
from io import BytesIO
from PIL import Image


# Not working for some reason I think it is because of the text and content are not suitable...
def getRequest(url, params=None):
    print(f"Getting request from {url}")
    req = request.get(url, params)
    if req.status_code == 200:
        print(f"Response: {req.text}")
        with open('03_image.jpeg', "w") as imgFile:
            imgFile.write(req.content)
    elif req.status_code == 400:
        print(f"Client Error: {req.status_code}")
    else:
        print(f"Error code: {req.status_code}")


# getRequest(f"http://www.tompetty.com/sites/g/files/g2000007521/f/hr10_sample_image_02_0.jpg")


# Using Image form PIL and BytesIO from io trying to store the image
def getRequest2(url, params=None):
    req = request.get(url, params)
    if req.status_code == 200:
        image = Image.open(BytesIO(req.content))
        imagePath = f"./03_image.{image.format}"
        print(f"Image parameters: ")
        print(f"    Resolution: {image.width}px * {image.height}px")
        print(f"    Width:    {image.width}")
        print(f"    Height:   {image.height}")
        print(f"    Format:   {image.format}")
        print(f"    Mode(col: {image.mode})")
        print(f"    Info:     {image.info}")
        # image.show() --> Open up the image
        # print(f"{image.size}, {image.format}, {image.mode}, {image.filename} {image.info}")
        try:
            image.save(imagePath, image.format)
        except IOError:
            print(f"Cannot save the image.")
    else:
        print(f"Check the status code: {req.status_code}")


getRequest2(f"http://newsfeedtemplate.netlify.com/img/photo03.jpg")
