import psycopg2, random

con = psycopg2.connect(dbname="flaskapp", user="flaskapp", password="Lt9wtCJbVyBFwGmz8Nxn")
con.autocommit = False
cur = con.cursor()

n = 10 * 1000
for i in range(n):
    cur.execute(f"INSERT INTO users VALUES ({i}, 'person{i}')")
for i in range(n):
    cur.execute(f"INSERT INTO presents VALUES ({i}, {random.randint(0, n-1)})")

con.commit()
cur.close()
con.close()