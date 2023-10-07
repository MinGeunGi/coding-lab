import sqlite3
con = sqlite3.connect('tutorial.db')

cur = con.cursor()

# cur.execute("CREATE TABLE movie(title, year, score)")

res = cur.execute("SELECT title, score, year FROM movie")
res.fetchone()

#print(res.fetchone())

cur.execute('''
  INSERT INTO movie VALUES
    ('엘리멘탈', 2023, 4.78),
    ('겨울왕국', 2014, 4.98)
''')
con.commit()

res = cur.execute("SELECT * FROM movie")
all_movie = res.fetchall() 
print(len(all_movie))

for movie in all_movie:
  print(movie[1])

  
con.close()

