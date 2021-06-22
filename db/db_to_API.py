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
for i in movies:
    movies_titles = PTN.parse(i)
    #print(movies_titles)


# API request matching
r = requests.get('https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query={}'.format(movies_titles['title']) #test more to get title matching

pprint.pprint(r.json())

print(movies_titles['title'])
