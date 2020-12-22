import requests

class Searchbykeyword:
    def __init__(self, query: str=None, searchapikey: str=None, page: int=None):
        self.query = query
        self.page = page
        self.searchapikey = searchapikey
        self.acception = {
            "accept": "application/json",
            "X-API-KEY": self.searchapikey
        }

    def searchbykeyword(self):
        if self.page == None:
            self.page = 1
        else:
            self.page

        if self.query == None:
            raise Exception("Query is not defined!")
        elif self.query:
            self.query

        searchbykeyword = requests.get(f"https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={self.query}&page={self.page}", headers=self.acception)
        return searchbykeyword

class Searchbyid:
    def __init__(self, filmid: int=None, searchapikey: str=None):
        self.filmid = filmid
        self.searchapikey = searchapikey
        self.acception = {
            "accept": "application/json",
            "X-API-KEY": self.searchapikey
        }

    def searchbyid(self):
        searchbyid = requests.get(f"https://kinopoiskapiunofficial.tech/api/v2.1/films/{self.filmid}", headers=self.acception)
        return searchbyid

class Searchdatabyid:
    def __init__(self, filmid: int=None, searchapikey: str=None):
        self.filmid = filmid
        self.searchapikey = searchapikey
        self.acception = {
            "accept": "application/json",
            "X-API-KEY": self.searchapikey
        }

        searchbyid = requests.get(f"https://kinopoiskapiunofficial.tech/api/v2.1/films/{self.filmid}", headers=self.acception)
        searchbyid = searchbyid.json()

        self.filmTitleru = searchbyid['data']['nameRu']
        self.filmTitleen = searchbyid['data']['nameEn']
        self.filmMainurlru = searchbyid['data']['webUrl']
        self.filmMainurlen = searchbyid['data']['webUrl']
        self.posterUrl = searchbyid['data']['posterUrl']
        self.posterUrlPreview = searchbyid['data']['posterUrlPreview']
        self.year = searchbyid['data']['year']
        self.filmLength = searchbyid['data']['filmLength']
        self.slogan = searchbyid['data']['slogan']
        self.description = searchbyid['data']['description']
        self.types = searchbyid['data']['type']
        self.ratingMpaa = searchbyid['data']['ratingMpaa']
        self.ratingAgeLimits = searchbyid['data']['ratingAgeLimits']
        self.premiereRu = searchbyid['data']['premiereRu']
        self.distributors = searchbyid['data']['distributors']
        self.premiereWorld = searchbyid['data']['premiereWorld']
        self.premiereDigital = searchbyid['data']['premiereDigital']
        self.premiereWorldCountry = searchbyid['data']['premiereWorldCountry']
        self.premiereDvd = searchbyid['data']['premiereDvd']
        self.premiereBluRay = searchbyid['data']['premiereBluRay']
        self.distributorRelease = searchbyid['data']['distributorRelease']
        self.countries = searchbyid['data']['countries'][0]['country']
        def genres():
            genres = list()
            for i in searchbyid['data']['genres']:
                genres.append(i['genre'])
            return genres
        self.genres = genres()
        self.facts = searchbyid['data']['facts']

# def searchbyfilters(self, genres: int=None, ratingfrom: int=None, ratingto: int=None, yearfrom: int=None, yearto: int=None, page: int=None):

#     searchbykeyword = {
#         "accept": "application/json",
#         "X-API-KEY": self.apikey
#     }

#     def genres(genres1=None):
#         heuta = {1: 1750, 2: 22, 3: 3, 4: 13, 5: 19, 6: 17, 7: 456, 8: 20, 9: 12, 10: 8, 11: 27, 12: 23, 13: 6, 14: 1747, 15: 15, 16: 16, 17: 7, 18: 21, 19: 14, 20: 9, 21: 28, 22: 10, 23: 25, 24: 11, 25: 24, 26: 26, 27: 4, 28: 1, 29: 2, 30: 18, 31: 5, 32: 1751}
#         if genres1 not in range(1, 33):
#             raise Exception(f"Index out of range!")
#         elif genres1 == None:
#             pass
#         else:
#             genres1 = heuta[genres1]
#             return f'&genre={genres1}'

#     def ratingfrom(ratingfrom1=None):
#         if ratingfrom1 not in range(1, 11):
#             raise Exception(f"Index out of range!")
#         elif ratingfrom1 == None:
#             pass
#         else:
#             return f'&ratingFrom={ratingfrom1}'

#     def ratingto(ratingto1=None):
#         if ratingto1 not in range(1, 11):
#             raise Exception(f"Index out of range!")
#         elif ratingto1 == None:
#             pass
#         else:
#             return f'&ratingTo={ratingto1}'

#     def yearfrom(yearfrom1=None):
#         if yearfrom1 == None:
#             pass
#         else:
#             yearfrom1 = f'&yearFrom={yearfrom1}'
#             return yearfrom1

#     def yearto(yearto1=None):
#         if yearto1 == None:
#             pass
#         else:
#             yearto1 = f'&yearTo={yearto1}'
#             return yearto1

#     def pages(page1=None):
#         if page1 == None:
#             page1 = '&page=1'
#             return page1 
#         else:
#             return f'&page={page1}'

#     searchbykeyword = requests.get(f"https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-filters?country={genres(genres)}{ratingfrom(ratingfrom)}{ratingto(ratingto)}{yearfrom(yearfrom)}{yearto(yearto)}{pages(pages)}", headers=searchbykeyword)
#     return searchbykeyword