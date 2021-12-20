import psycopg2

con = psycopg2.connect(dbname="flaskapp", user="flaskapp", password="Lt9wtCJbVyBFwGmz8Nxn")
con.autocommit = False
cur = con.cursor()

cur.execute('SELECT id, (SELECT COUNT(*) FROM presents WHERE user_to = id) as received FROM users ORDER BY received DESC LIMIT 10')
# a co jeśli zrobimy to bez podzapytania, tylko joinem?
# cur.execute('select id, count(*) from users join presents on id = user_to group by id order by count(*) desc limit 10')
print(cur.fetchall())

cur.close()
con.close()