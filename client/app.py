from flask import Flask, render_template, url_for, redirect, request
import requests

app = Flask(__name__)

@app.route('/movie', methods=['POST'])
def MovieDetails():
    movieTitle = request.form['movieTitle']
    r_movie = 'https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query={}'.format(movieTitle)
    r = requests.get(r_movie)
    movieDetails = r.text
    return render_template('movie.html', movieDetails=movieDetails)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)