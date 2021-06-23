import requests, sqlite3, PTN, pprint

# setting connection to db
conn = sqlite3.connect('local-movies.db')
cur = conn.cursor() 

# query and variable assignment for movies
qry = """SELECT * FROM movies"""
cur.execute(qry)
# TODO - issue - should be no '+' on the end of title where ' ' in left
movies = [i[0].replace(' ', '+') for i in cur.fetchall()] # stores all movies in list


# parse all movies into specfic dict naming convention for API matching
movies_titles = []
for i in movies:
    movies_parse = PTN.parse(i)
    movies_titles.append(movies_parse)

#pprint.pprint(movies_titles)


# API request matching

movie_detials = []
for dic in movies_titles:
    for key in dic:
          if dic[key] == dic['title']:
                  movie_req = 'https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query={}'.format(dic['title'])
                  #print(movie_req)
                  r = requests.get(movie_req)
                  #pprint.pprint(r.json())
                  movie_detials.append(r.json())

pprint.pprint(movie_detials)

