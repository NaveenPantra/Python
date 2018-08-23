import requests as request
from bs4 import BeautifulSoup as bs


class GetTitles(object):
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

    def __init__(self, title):
        self.title = title
        self.url = f"https://www.imdb.com"
        self.titleResultTerms = {
            f"titleTable": f".findList",
            f"link": 'a',
        }
        self.imageLinks = []
        self.movieLinks = []
        self.params = {
            f"q": title,
        }
        self.getPage()

    def getPage(self):
        res = request.get(f"{self.url}/find", self.params)
        print(f"Page URL: {res.url}")
        soup = bs(res.text, 'lxml')
        # soup.select(self.titleResultTerms['titleTable'])[0].select('img')[0]['src']
        resultCount = soup.select(self.titleResultTerms['titleTable'])[0]
        # print(f"{len(resultCount)}")
        link = 0
        for row in range(len(resultCount) - 1):
            self.imageLinks.append(soup.select(self.titleResultTerms['titleTable'])[0].select('img')[row]['src'])
            self.movieLinks.append(f"{self.url}{soup.select(self.titleResultTerms['titleTable'])[0].select('a')[link]['href']}")
            link += 2
        print(f"Movie Links: {self.movieLinks}\nImage Links: {self.imageLinks}")


getTitle = GetTitles("Dhoom")
