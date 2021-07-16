import os, csv

path = 'F:\Movies-TV'

with open('C:\wsl\local-movies\db\movies.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  for root,dirs, files in os.walk(path):
      for folders in dirs:
          if folders == "Subs" or folders == "Subtitles" or folders == "Other" or folders == "subtitles":
            pass
          else:
            writer.writerow([folders.replace('.', ' ')])