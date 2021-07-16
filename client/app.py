from flask import Flask, render_template, url_for, redirect, request
import PTN, sqlite3, json, os, requests

app = Flask(__name__)

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


@app.route('/movie', methods=['POST'])
def displayMovies():     
    """
    reads json file with list of nested dict to display 
    """
    URL = 'https://image.tmdb.org/t/p/w300'

    with open('data.json') as file:
        movieDetails = json.load(file)
                       
    return render_template('movie.html',
    movieDetails=movieDetails,
    URL=URL)


@app.route('/')
def index():

	return render_template('index.html')



@app.route('/updateMovies/')
def updateMovies():
    """
    this function acts as a refresh for any new movies added to your directory
    """
    movieDetails = []
    for dic in movie_titles:            
        for key in dic:
            if dic[key] == dic['title']:
                movie_req = 'https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query={}&year={}'.format(dic['title'], dic['year'])
                r = requests.get(movie_req)
                movie_detials = r.json()
                    
                # selection of key and values
                detials = []
                for key, value in movie_detials.items():
                    if key == 'results':
                        detials = value

                # parsing movieDetials 
                movieTitle = next((item['title'] for item in detials), None)   
                movieRating = next((item['vote_average'] for item in detials), None)
                movieYear = next((item['release_date'] for item in detials), None)
                movieOverview = next((item['overview'] for item in detials), None)
                movieImage = next((item['poster_path'] for item in detials), None)
                    
                # creating a list of nested dict for json file full of movieDetials to be used in movie template
                movie_dict = {"title": movieTitle, "year": movieYear, "rating": movieRating, "overview": movieOverview, "image": movieImage}
                movieDetails.append(movie_dict.copy())

    with open('./data.json', 'w') as file:
        json.dump(movieDetails, file, indent=4)

    return render_template('index.html')


@app.route('/filepath/')
def filepath():
    """
    set file path for movie directory
    """
    path = "E:\Tv&Movies\Movies"
    path = os.path.realpath(path)
    movieBrowse = os.startfile(path)
    return render_template('movie.html', movieBrowse=movieBrowse)

if __name__ == '__main__':
    app.run(debug=True)