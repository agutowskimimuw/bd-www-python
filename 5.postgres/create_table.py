import psycopg2

con = psycopg2.connect(dbname="flaskapp", user="flaskapp", password="Lt9wtCJbVyBFwGmz8Nxn")
cur = con.cursor()

cur.execute('''CREATE TABLE things (
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    date DATE
);''')

cur.execute("INSERT INTO things VALUES (0, 'apple', '2021-12-12')")
cur.execute("INSERT INTO things VALUES (1, 'banana', NULL)")

con.commit()

cur.close()
con.close()

print('Stworzono tabelę "things"!')
