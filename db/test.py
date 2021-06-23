import requests, sqlite3, PTN, pprint

movies = [
    {
    "year": 2014,
    "quality": "HDRip",
    "codec": "XViD",
    "title": "Dawn+of+the+Planet+of+the+Apes"
    },
    {
    'group': 'JYK',
    'title': 'San+Andreas',
    'resolution': '720p',
    'codec': 'x264',
    'year':  '2015',
    'audio': 'AAC',
    'quality': 'WEB-DL'
    }
  ]

# API request matching
#movie_req = ['https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query={}'.format(movies[0]['title'])]
#r = requests.get(movie_req)
#pprint.pprint(r.json())
  

#r = requests.get(movie_req)
#pprint.pprint(r.json())
#print('https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query={}'.format(movies[1]['title']))
  
movie_detials = []
for dic in movies:
    for key in dic:
          if dic[key] == dic['title']:
                  movie_req = 'https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query={}'.format(dic['title'])
                  #print(movie_req)
                  r = requests.get(movie_req)
                  #pprint.pprint(r.json())
                  movie_detials.append(r.json())

pprint.pprint(movie_detials)
#r = requests.get(movie_req)
                
      