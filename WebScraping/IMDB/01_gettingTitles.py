import requests as request
from bs4 import BeautifulSoup as bs


class GetTitles(object):
    def __init__(self, title):
        self.title = title
        self.url = f"https://www.imdb.com/find"
        self.titleResultTerms = {
            f"titleTable": f".findList",
            f"link": 'a',
        }
        self.params = {
            f"q": title,
        }
        self.getPage()

    def getPage(self):
        res = request.get(self.url, self.params)
        print(f"Page URL: {res.url}")
        soup = bs(res.text, 'lxml')
        with open('01_index.html', "w") as file:
            file.write(res.text)
        # Get the Result for the movies
        """
            Structure of the Relevant titles in for the search string 
            findList[0] +/
                +/ <a href = "same"> <img src = "Poster"> </a>   <a href = "same"></a>
                +/ <a href = "same"> <img src = "Poster"> </a>   <a href = "same"></a>
                +/ <a href = "same"> <img src = "Poster"> </a>   <a href = "same"></a>
                +/ <a href = "same"> <img src = "Poster"> </a>   <a href = "same"></a>
                .
                .
                .
        """

        table = soup.select(self.titleResultTerms['titleTable'])[0]
        # titleResult = soup.select(self.titleResultTerms['titleTable'])[0].select('img')[0]['src']
        for row in table:
            


getTitle = GetTitles("Dhoom")
