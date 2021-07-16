# Local-movies
local movie host that matches titles with movie api attributes/details
* Run the flask app to see setup instructions

# Resources used
* [The Movie Database (TMDb) API](https://www.themoviedb.org/)

* [PTN](https://github.com/divijbindlish/parse-torrent-name)

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)


![Local-Movies-App](https://github.com/JontyBurden/local-movies/blob/main/local-movies-app.png)

# Current Issues and Future Features
* Only have Browse button to browse movies dir when hover state on movie card
* <key error: 'year'> for matching local movie data with API year (this will occur when the format of the orginal movie doesn't match with PTN e.g. very strict formatting required.
* Update movie button needs to remove current data.json to update to new movie json (or some other way to add only new movies the data.json)
* Might make executable-flask-pyinstaller for app (https://elc.github.io/posts/executable-flask-pyinstaller/)