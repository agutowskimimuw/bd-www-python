import psycopg2
from transactions import prepare_db, begin_transaction

prepare_db()

t0 = begin_transaction('t0', isolation_level=1)
t0.insert(1)
t0.commit()

t1 = begin_transaction('t1', isolation_level=1)
t1.delete_all(1)
t1.select()
t1.rollback()

t2 = begin_transaction('t2', isolation_level=1)
t2.select()
t2.close()
