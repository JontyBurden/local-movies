import requests, json


r  = 'https://api.themoviedb.org/3/search/movie?api_key=4cc1b68a07fe5ba265950e85ac96cb2c&query=Jack+Reacher'

movie_req = requests.get(r)
data = movie_req.json()

movieTitle = data.get('result', {})


d = {"page":1,"results":
[{"adult":"false","backdrop_path":"/k7h4RNAarfOrF2r2YMN0P2FQSr4.jpg","genre_ids":[80,18,53,28],"id":75780,"original_language":"en","original_title":"Jack Reacher","poster_path":"/zlyhKMi2aLk25nOHnNm43MpZMtQ.jpg","release_date":"2012-12-20","title":"Jack Reacher"}], "total_pages":1,"total_results":2}

test = []
for key, value in d.items():
    if key == 'results':
        test = value

img_src = 'https://image.tmdb.org/t/p/w500'
print(img_src + test[0]['poster_path'])

