import psycopg2, random

con = psycopg2.connect(dbname="flaskapp", user="flaskapp", password="Lt9wtCJbVyBFwGmz8Nxn")
con.autocommit = False
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS presents CASCADE')
cur.execute('DROP TABLE IF EXISTS users CASCADE')

cur.execute('''CREATE TABLE users (
    id INT PRIMARY KEY,
    name TEXT
);''')

cur.execute('''CREATE TABLE presents (
    user_from INT REFERENCES users,
    user_to INT REFERENCES users
);''')

con.commit()

cur.close()
con.close()

print('Stworzono tabele "users" i "presents"!')
