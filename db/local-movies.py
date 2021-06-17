import sqlite3, csv

class csv_read(object):
    #source - Paul Rooney(https://stackoverflow.com/questions/31243618/python-import-csv-to-sqlite)

    def csv_file(self):
        self.readFile('movies.csv')

    def readFile(self, filename):
        conn = sqlite3.connect('local-movies.db')
        cur = conn.cursor() 
        cur.execute("""CREATE TABLE IF NOT EXISTS movies (movie_title varchar)""")
        filename.encode('utf-8')
        with open(filename) as f:
            reader = csv.reader(f)
            for field in reader:
                cur.execute("""INSERT INTO movies VALUES (?);""", field)

        conn.commit()
        conn.close()

c = csv_read().csv_file()