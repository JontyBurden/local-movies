import requests, json


r  = 'https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query=Jack+Reacher'

movie_req = requests.get(r)
response = movie_req.text
data = json.loads(response)
#print(data)
