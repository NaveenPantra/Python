import requests as request
from bs4 import BeautifulSoup as bs
import re
from pymongo import MongoClient
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError

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


class StoreTitles(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.movie
        self.titles = self.db.titles
        self.makeUnique()

    def makeUnique(self):
        self.db.titles.create_index([('movie_id', ASCENDING)], unique=True)

    def insertDocument(self, docs):
        print(len(docs))
        for doc in docs:
            try:
                self.titles.insert(doc)
            except DuplicateKeyError:
                print(f"{doc} is already in DB")
                print(f"{self.titles.find({'movie_id': doc['movie_id']})}")


class GetTitles(object):
    # Get the Result for the movies
    def __init__(self, title, quan):
        self.db = StoreTitles()
        self.title = title
        self.url = f"https://www.imdb.com"
        self.titleResultTerms = {
            f"titleTable": f".findList",
            f"link": 'a',
        }
        self.imageLinks = []
        self.movieLinks = []
        self.paramsL = {
            f"q": title,
            f"s": f"tt",
        }
        self.paramsS = {
            f"q": title,
        }
        # self.result = {}
        self.result = []
        if quan in ['s', 'S', 'sort', 'SORT', 'Sort']:
            self.getPage(self.paramsS)
        else:
            self.getPage(self.paramsL)

    # https://www.imdb.com/find?q=...
    def getPage(self, params):
        res = request.get(f"{self.url}/find", params)
        print(f"Page URL: {res.url}")
        soup = bs(res.text, 'lxml')

        # Get Result Title names
        # tt = 0
        # for section in soup.select('.findSection'):
        #     name = section.select('a')[0]['name']
        #     if name == 'tt':
        #         break
        #     tt += 1

        titleLinks = soup.select('.findSection')[0].select('.result_text')
        titleNames = []
        for title in titleLinks:
            titleNames.append(title.select('a')[0].string.replace(':', " "))
        print(titleNames)

        # soup.select(self.titleResultTerms['titleTable'])[0].select('img')[0]['src']
        resultCount = soup.select(self.titleResultTerms['titleTable'])[0]
        link = 0
        for row in range(len(resultCount) - 1):
            self.imageLinks.append(soup.select(self.titleResultTerms['titleTable'])[0].select('img')[row]['src'])
            self.movieLinks.append(
                f"{self.url}{soup.select(self.titleResultTerms['titleTable'])[0].select('a')[link]['href']}")
            link += 2
        print(f"Movies found: {len(self.movieLinks)}: {self.movieLinks}")
        index = 0
        for movieUrl in self.movieLinks:
            movie = self.getMovieDetails(movieUrl, titleNames[index])
            print(f"{movieUrl}: {movie}")
            self.addResult(titleNames[index], movie)
            index += 1
        # print(self.result)
        self.db.insertDocument(self.result)
        # self.display()

    # For debugging purpose
    # def display(self):
    #     for key, value in self.result.items():
    #         print(f"{key}: {value}")

    # To check the movie tile consist like
        # Dhoom
        # Dhoom now this will change to Dhoom 1,
        # Dhoom now this will change to Dhoom 2 and so on.
    def addResult(self, title, movie):
        # if title in self.result:
        #     for i in range(1, 100):
        #         if title + f"({i})" not in self.result:
        #             title += f"({i})"
        #             break
        # self.result[title] = movie
        self.result.append(movie)

    @staticmethod
    def getMovieDetails(movieUrl, movieTitle):
        movie = {
            "movie_id": "",
            "title": movieTitle,
            "poster": "",
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

        # movie_ID
        # URL: https://www.imdb.com/title/tt5770786/?ref_=fn_tt_tt_7
        # Regex: tt[0-9]+
        regex = r"tt[0-9]+"
        movie_id = re.findall(regex, movieUrl)
        movie["movie_id"] = movie_id[0]

        # Poster
        try:
            movie["poster"] = soup.select('.poster img')[0]['src']
        except IndexError:
            pass

        # Get Rating
        try:
            movie['rating']['ratingValue'] = soup.select('.imdbRating span')[0].string
            movie['rating']['ratingTotal'] = soup.select('.imdbRating span')[2].string
            movie['rating']['votesTotal'] = soup.select('.imdbRating span')[3].string
            movie['rating']['critics'] = soup.select('.imdbRating span')[-1].string
        except IndexError:
            pass

        # Movie Information
        try:
            movie['duration'] = soup.select('.subtext time')[0].string.strip()
            genre = soup.select('.subtext a')[:-1]
            for typeGenre in genre:
                movie['genre'].append(typeGenre.string)
            movie['release'] = soup.select('.subtext a')[-1].string.strip()
        except IndexError:
            pass

        # Story line
        try:
            movie['storyLine'] = soup.select('.summary_text')[0].string.strip()
        except IndexError:
            pass
        except AttributeError:
            pass

        # Crew
        i = 0
        try:
            movie['crew']['director'] = soup.select('.credit_summary_item')[i].select('a')[0].string
            i += 1
        except IndexError:
            pass
        try:
            if soup.select('.credit_summary_item')[i].select('h4')[0].string.strip() in ["Writers:", "Writer:"]:
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
        except IndexError:
            pass
        except AttributeError:
            pass

        return movie


title = input("ENTER TITLE: ")
quan = input("Result Length (short/long) (s/l): ")
getTitle = GetTitles(title, quan)

# self.movie = {
#             "poster": "Poster URL"
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
