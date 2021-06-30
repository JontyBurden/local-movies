from flask import Flask, render_template, url_for, redirect, request
import requests
import PTN, sqlite3

app = Flask(__name__)

# setting connection to db
path = 'C:\wsl\local-movies\db\local-movies.db'
conn = sqlite3.connect(path)
cur = conn.cursor() 

# query and variable assignment for movies
qry = """SELECT * FROM movies"""
cur.execute(qry)

# stores all movies in list
movies = [i[0].replace(' ', '+') for i in cur.fetchall()] # stores all movies in list

# parse all movies into specfic dict naming convention for API matching
movie_titles = []
for i in movies:
    movie_parse = PTN.parse(i)
    movie_titles.append(movie_parse)

@app.route('/movie', methods=['POST'])
def MovieDetails():     
    """
    takes db qry of all movies and handles API requests for each matching both movie tile and year
    """
    URL = 'https://image.tmdb.org/t/p/w300'

    # matching movie titles from db qry to API calls
    movieDetails = []
    for dic in movie_titles:            
        for key in dic:                  
                if dic[key] == dic['title']:                    
                    movie_req = 'https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query={}&year={}'.format(dic["title"], dic["year"])
                    r = requests.get(movie_req)
                    movie_detials = r.json()
                    
                    # selection of key and values
                    test = []
                    for key, value in movie_detials.items():
                        if key == 'results':
                            test = value

                    # parsing movieDetials 
                    movieTitle = next((item['title'] for item in test), None)   
                    movieRating = next((item['vote_average'] for item in test), None)
                    movieYear = next((item['release_date'] for item in test), None)
                    movieOverview = next((item['overview'] for item in test), None)
                    movieImage = next((item['poster_path'] for item in test), None)
                    
                    # creating a list of nested dict for movieDetials
                    movie_dict = {"title": movieTitle, "year": movieYear, "rating": movieRating, "overview": movieOverview, "image": movieImage}
                    movieDetails.append(movie_dict.copy())
                          
    return render_template('movie.html',
    movieDetails=movieDetails,
    URL=URL)

@app.route('/')
def index():

	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)