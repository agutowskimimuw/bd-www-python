import psycopg2

con = psycopg2.connect(dbname="flaskapp", user="flaskapp", password="Lt9wtCJbVyBFwGmz8Nxn")
con.autocommit = False
cur = con.cursor()

cur.execute('CREATE INDEX abc ON presents (user_to)')

con.commit()
cur.close()
con.close()