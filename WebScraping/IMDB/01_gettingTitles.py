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
        self.getPage()

    def getPage(self):
        res = request.get(f"{self.url}/find", self.params)
        print(f"Page URL: {res.url}")
        soup = bs(res.text, 'lxml')

        # Get Result Title names
        titleLinks = soup.select('.findSection')[0].select('.result_text')
        titleNames = []
        for title in titleLinks:
            titleNames.append(title.select('a')[0].string.replace(':', " "))

        # soup.select(self.titleResultTerms['titleTable'])[0].select('img')[0]['src']
        resultCount = soup.select(self.titleResultTerms['titleTable'])[0]
        # print(f"{len(resultCount)}")
        link = 0
        for row in range(len(resultCount) - 1):
            self.imageLinks.append(soup.select(self.titleResultTerms['titleTable'])[0].select('img')[row]['src'])
            self.movieLinks.append(
                f"{self.url}{soup.select(self.titleResultTerms['titleTable'])[0].select('a')[link]['href']}")
            link += 2
        index = 0
        for movieUrl in self.movieLinks:
            movie = self.getMovieDetails(movieUrl)
            self.addResult(titleNames[index], movie)
            index += 1
        self.display()

    def display(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def addResult(self, title, movie):
        self.result[title] = movie

    @staticmethod
    def getMovieDetails(movieUrl):
        movie = {
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
        res = request.get(movieUrl)
        soup = bs(res.text, 'lxml')

        # Get Rating
        movie['rating']['ratingValue'] = soup.select('.imdbRating span')[0].string
        movie['rating']['ratingTotal'] = soup.select('.imdbRating span')[2].string
        movie['rating']['votesTotal'] = soup.select('.imdbRating span')[3].string
        movie['rating']['critics'] = soup.select('.imdbRating span')[-1].string

        # Movie Information
        movie['duration'] = soup.select('.subtext time')[0].string.strip()
        genre = soup.select('.subtext a')[:-1]
        for typeGenre in genre:
            movie['genre'].append(typeGenre.string)
        movie['release'] = soup.select('.subtext a')[-1].string.strip()

        # Story line
        movie['storyLine'] = soup.select('.summary_text')[0].string.strip()

        # Crew
        i = 0
        movie['crew']['director'] = soup.select('.credit_summary_item')[i].select('a')[0].string
        i += 1
        try:
            if soup.select('.credit_summary_item')[i].select('h4')[0].string.strip() == "Writers:":
                for writer in soup.select('.credit_summary_item')[i].select('a'):
                    movie['crew']['writer'].append(writer.string)
                i += 1
        except IndexError:
            pass
        try:
            for cast in soup.select('.credit_summary_item')[i].select('a'):
                movie['crew']['stars'].append(cast.string)
            movie['crew']['stars'].pop()
        except IndexError:
            pass

        # Awards
        # Changing exception if anything occur
        try:
            movie['awards'] = soup.select('.awards-blurb')[0].string.strip()
        except:
            pass

        return movie


title = input("ENTER TITLE: ")
getTitle = GetTitles('dhoom')

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
