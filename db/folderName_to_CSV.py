import os, csv

path = 'E:\Tv&Movies\Movies' #TODO: Setup with widget to select path from given user

with open('C:\wsl\local-movies\db\movies.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  for root,dirs, files in os.walk(path):
      for folders in dirs:
          if folders == "Subs" or folders == "Subtitles" or folders == "Other" or folders == "subtitles": # TODO: better way to skip non-movie names
            pass
          else:
            writer.writerow([folders.replace('.', ' ')])