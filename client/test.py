import PTN, sqlite3, json, os, requests, pprint

# setting connection to db
path = 'C:\wsl\local-movies\db\local-movies.db'
conn = sqlite3.connect(path)
cur = conn.cursor() 

# query and variable assignment for movies
qry = """SELECT * FROM movies"""
cur.execute(qry)

# stores all movies in list
movies = [i[0] for i in cur.fetchall()] # stores all movies in list

# parse all movies into specfic dict naming convention for API matching
movie_titles = []
for i in movies:
    movie_parse = PTN.parse(i)
    movie_titles.append(movie_parse)

print(pprint.pprint(movie_titles))