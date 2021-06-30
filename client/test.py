import requests, json, pprint

"""
place for testing features

"""
r  = 'https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query=Jack+Reacher'

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
    },
    {
   'group': '0-FGT',
     'title': 'The Martian',
     'resolution': '540p',
     'excess': ['KORSUB', '2'],
     'codec': 'x264',
     'year': 2015,
     'audio': 'AAC',
     'quality': 'HDRip'
    },
    {
    "year": 2000,
    "quality": "HDRip",
    "codec": "XViD",
    "title": "Gladiator"
    },
    {
    "year": 2003,
    "quality": "HDRip",
    "codec": "XViD",
    "title": "Oldboy"
    },
    {
    "year": 2019,
    "quality": "HDRip",
    "codec": "XViD",
    "title": "A+Sun"
    }
  ]

d = {"page":1,"results":
[{"adult":"false","backdrop_path":"/k7h4RNAarfOrF2r2YMN0P2FQSr4.jpg","genre_ids":[80,18,53,28],"id":75780,"original_language":"en","original_title":"Jack Reacher","poster_path":"/zlyhKMi2aLk25nOHnNm43MpZMtQ.jpg","release_date":"2012-12-20","title":"Jack Reacher"}], "total_pages":1,"total_results":2}

def getMovieDetails(movie_titles):
      
    """
    takes db qry of all movies and handles API requests for each matching both movie tile and year
    """
    movieDetails = []
    for dic in movie_titles:            
        for key in dic:                  
                if dic[key] == dic['title']:                    
                    movie_req = 'https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query={}&year={}'.format(dic['title'],dic['year'])
                    r = requests.get(movie_req)
                    movie_detials = r.json()
                    #print(movie_detials)
                    # selection of key and values
                    test = []
                    for key, value in movie_detials.items():
                        if key == 'results':
                            test = value

                    movieTitle = next((item['title'] for item in test), None)
    
                    movieRating = next((item['vote_average'] for item in test), None)

                    movieYear = next((item['release_date'] for item in test), None)

                    movieOverview = next((item['overview'] for item in test), None)
                    

                    
                    movie_dict = {"title": movieTitle, "year": movieYear, "movieRating": movieRating, "overview": movieOverview}
                    movieDetails.append(movie_dict.copy())
    #print(movieDetails)
    print(movieDetails)
        
    
    
    #print(titles)

                    
    
getMovieDetails(movie_titles)



