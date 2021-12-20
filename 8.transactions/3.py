import psycopg2
from transactions import prepare_db, begin_transaction

prepare_db()

t1 = begin_transaction('t1', isolation_level=1)
t1.insert(1)
t1.select()
t1.rollback()

t2 = begin_transaction('t2', isolation_level=1)
t2.select()
t2.close()
