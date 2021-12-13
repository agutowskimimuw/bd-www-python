import psycopg2

con = psycopg2.connect(dbname="flaskapp", user="flaskapp", password="Lt9wtCJbVyBFwGmz8Nxn")
cur = con.cursor()

cur.execute("SELECT * FROM things")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
con.close()
