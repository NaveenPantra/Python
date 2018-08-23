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
        self.result = {}
        self.movie = {
            "rating": {
                "ratingValue": 0,
                "ratingTotal": 0,
                "votesTotal": 0,
                "critics": 0,
            },
            "genre": [],
            "duration": "",
            "release": "",
            "storyLine": "",
            "crew": {
                "director": [],
                "writer": [],
                "stars": [],
            },
            "awards": "",
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
            self.movieLinks.append(
                f"{self.url}{soup.select(self.titleResultTerms['titleTable'])[0].select('a')[link]['href']}")
            link += 2
        for movieUrl in self.movieLinks:
            self.getMovieDetails(movieUrl)

    def getMovieDetails(self, movieUrl):
        res = request.get(movieUrl)
        soup = bs(res.text, 'lxml')

        # Get Rating
        self.movie['rating']['ratingValue'] = soup.select('.imdbRating span')[0].string
        self.movie['rating']['ratingTotal'] = soup.select('.imdbRating span')[2].string
        self.movie['rating']['votesTotal'] = soup.select('.imdbRating span')[3].string
        self.movie['rating']['critics'] = soup.select('.imdbRating span')[-1].string

        # Movie Information
        self.movie['duration'] = soup.select('.subtext time')[0].string.strip()
        genre = soup.select('.subtext a')[:-1]
        for type in genre:
            
        self.movie['release'] = soup.select('.subtext a')[-1].string.strip()
        print(f"{self.movie}")



getTitle = GetTitles("Dhoom")


# self.movie = {
#             "rating": {
#                 "ratingValue": 0,
#                 "ratingTotal": 0,
#                 "votesTotal": 0,
#                 "critics": 0,
#             },
#             "genre": [],
#             "duration": "",
#             "release": "",
#             "storyLine": "",
#             "crew": {
#                 "director": [],
#                 "writer": [],
#                 "stars": [],
#             },
#             "awards": "",
#         }
