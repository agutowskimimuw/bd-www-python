import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

cur.execute("SELECT * FROM things")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
con.close()
