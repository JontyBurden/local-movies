import requests, sqlite3, PTN, pprint, json

# setting connection to db
conn = sqlite3.connect('local-movies.db')
cur = conn.cursor() 

# query and variable assignment for movies
qry = """SELECT * FROM movies"""
cur.execute(qry)
# TODO - issue - should be no '+' on the end of title where ' ' in left
movies = [i[0].replace(' ', '+') for i in cur.fetchall()] # stores all movies in list


# parse all movies into specfic dict naming convention for API matching
movie_titles = []
for i in movies:
    movie_parse = PTN.parse(i)
    movie_titles.append(movie_parse)

pprint.pprint(movie_titles)


# API request matching

def getMovieDetails(movie_titles):
  
    """
    takes db qry of all movies and handles API requests for each matching both movie tile and year
    """
    movie_detials = []
    for dic in movie_titles:            
        for key in dic:                  
                if dic[key] == dic['title']:                    
                    movie_req = 'https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query={}&year={}'.format(dic["title"], dic["year"])
                    r = requests.get(movie_req)
                    movie_detials = r.json()
                    pprint.pprint(r.json())
    #pprint.pprint(movie_detials)
#getMovieDetails(movie_titles)


