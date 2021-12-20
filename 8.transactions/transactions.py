import psycopg2
from multiprocessing import Process

class Transaction:
    def __init__(self, name, con):
        self.name = name
        self.con = con
        self.cur = con.cursor()
    
    def insert(self, val):
        self.cur.execute('INSERT INTO t VALUES (%s)', (val,))
        print(f'transakcja {self.name}: INSERT INTO t VALUES ({val});')
    
    def select(self):
        self.cur.execute('SELECT * FROM t')
        rows = self.cur.fetchall()
        print(f'transakcja {self.name}: SELECT * FROM t; wynik: [' + ', '.join(str(row[0]) for row in rows) + ']')
        return rows
    
    def replace_all(self, val_prev, val_next):
        self.cur.execute('UPDATE t SET val = %s WHERE val = %s', (val_next, val_prev))
        print(f'transakcja {self.name}: UPDATE t SET val = {val_next} WHERE val = {val_prev};')
    
    def delete_all(self, val):
        self.cur.execute('DELETE FROM t WHERE val = %s', (val,))
        print(f'transakcja {self.name}: DELETE FROM t WHERE val = {val};')


    def commit(self):
        print(f'transakcja {self.name}: COMMIT')
        self.con.commit()
        self.cur.close()
        self.con.close()
    
    def rollback(self):
        print(f'transakcja {self.name}: ROLLBACK')
        self.con.rollback()
        self.cur.close()
        self.con.close()
    
    def close(self):
        self.cur.close()
        self.con.close()

def connect():
    return psycopg2.connect(dbname="flaskapp", user="flaskapp", password="Lt9wtCJbVyBFwGmz8Nxn")

def prepare_db(unique_values=False):
    con = connect()
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS t")
    if unique_values:
        cur.execute("CREATE TABLE t (val INT PRIMARY KEY)")
    else:
        cur.execute("CREATE TABLE t (val INT)")
    con.commit()
    cur.close()
    con.close()

def begin_transaction(name, isolation_level, readonly=False):
    con = connect()
    con.autocommit = False
    con.set_session(isolation_level=isolation_level, readonly=False)
    print(f'poziom izolacji transakcji {name}: {isolation_level}')
    return Transaction(name, con)

def run_in_parallel(*funs):
    threads = [Process(target=f) for f in funs]
    for thr in threads: thr.start()
    for thr in threads: thr.join()
