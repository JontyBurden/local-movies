from flask import Flask, render_template, url_for, redirect, request
import requests

app = Flask(__name__)

#test cases for API matching and front-end display
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

@app.route('/movie', methods=['POST'])
def MovieDetails():     
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
                    
                    # creating a list of nested dict for movieDetials
                    movie_dict = {"title": movieTitle, "year": movieYear, "rating": movieRating, "overview": movieOverview}
                    movieDetails.append(movie_dict.copy())
                          
    return render_template('movie.html',
    movieDetails=movieDetails)

@app.route('/')
def index():

	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)