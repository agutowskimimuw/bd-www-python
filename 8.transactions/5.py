import psycopg2
from transactions import prepare_db, begin_transaction, run_in_parallel

prepare_db()

t0 = begin_transaction('t0', isolation_level=1)
t0.insert(1)
t0.insert(2)
t0.select()
t0.commit()

import time

def run_t1():
    t1 = begin_transaction('t1', isolation_level=3)
    t1.replace_all(1, 2)
    time.sleep(2)
    t1.commit()

def run_t2():
    time.sleep(1)
    t2 = begin_transaction('t2', isolation_level=3)
    t2.replace_all(2, 1)
    t2.commit()

run_in_parallel(run_t1, run_t2)

t3 = begin_transaction('t3', isolation_level=1)
t3.select()
t3.close()
