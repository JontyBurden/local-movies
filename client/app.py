from flask import Flask, render_template, url_for, redirect, request
import requests

app = Flask(__name__)

@app.route('/movie', methods=['POST'])
def MovieDetails():
    #img_src = 'https://image.tmdb.org/t/p/w500'
    r = 'https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query=Jack+Reacher'
    movie_req = requests.get(r)
    d = movie_req.json()
    movieDetails = []
    for key, value in d.items():
        if key == 'results':
            movieDetails = value
    movieTitle = movieDetails[0]['title']
    movieDescp = movieDetails[0]['overview']
    movieRating = movieDetails[0]['vote_average']
    #movieImage = img_src + MovieDetails[0]['poster_path']
    return render_template('movie.html', 
    movieTitle=movieTitle,     
    movieDescp=movieDescp,
    movieRating=movieRating)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)