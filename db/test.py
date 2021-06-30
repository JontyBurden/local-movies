import requests, sqlite3, PTN, pprint, json

movie_titles = [
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

def getMovieDetails(movie_titles):
      
    """
    takes db qry of all movies and handles API requests for each matching both
    movie tile and year
    """
    movie_detials = []
    for dic in movie_titles:            
        for key in dic:                  
                if dic[key] == dic['title']:                    
                    movie_req = 'https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query={}&year={}'.format(dic['title'],dic['year'])
                    r = requests.get(movie_req)
                    movie_detials.append(r.json())
    return movie_detials
    #pprint.pprint(movie_detials) # shows json struc with movies detials

getMovieDetails(movie_titles)


# Reading through JSON struc (nested list of nest dict)

def displayMovieKeyValues(getMovieDetails):
    """
    to display values with flask we must be able to iterate through a dictionary to display things such as title, movie_poster, movie_rating, etc.
    """


    for k1,v1 in getMovieDetails.items():
        temp = ""   
        temp+=k1
        for k2,v2 in v1.items():
           temp = temp+" "+str(k2)+" "+str(v2)
        print(temp)

displayMovieKeyValues(getMovieDetails(movie_titles))

    
