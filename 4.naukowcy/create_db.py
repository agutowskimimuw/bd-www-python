import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

with open('naukowcy.sql', 'r') as f:
    cur.executescript(f.read())

con.commit()

cur.close()
con.close()

print('Stworzono bazę danych w pliku db.sqlite3!')
