import requests
from pprint import pprint

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"



headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "a55fbe10bdmshc8beedf86245939p183b0djsn9fc3c8f22f9f"
    }

'''
for el in testing:
    querystring = {"page":"1","r":"json","s":f"{el}"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    pprint(response.text)
'''

querystring = {"page": "1", "r": "json", "s": "Tribe"}
response = requests.request("GET", url, headers=headers, params=querystring)
pprint()