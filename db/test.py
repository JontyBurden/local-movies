"""
Plan -
  import files to csv and change . to ' ' with .replace
  import into database
  iterate and read through db with PIN library to match 'title' and 'year' with api
  select API data
  do something with flask
"""
movies = [
    {
    "year": 2014,
    "resolution": "1080p",
    "quality": "BrRip",
    "codec": "H264",
    "excess": "",
    "title": "Hercules"
    },
    {
    "year": 2014,
    "quality": "HDRip",
    "codec": "XViD",
    "title": "Dawn of the Planet of the Apes"
    }
  ]

# Extract info for API to match
movie_titles = [n['title'] for n in movies]
#print(movie_titles)

import PTN

info = PTN.parse('San Andreas 2015 720p WEB-DL x264 AAC-JYK')

print(info) # All details that were parsed

  