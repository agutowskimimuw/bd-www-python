import psycopg2
from transactions import prepare_db, begin_transaction

prepare_db()

# isolation_level przyjmuje wartości od 1 do 3 (może też być 4, ale to oznacza "default")
# zadanie: zbadać, na jakie niepożądane zjawiska pozwala dany poziom izolacji
# (dirty read, non-repeatable read, phantom read)
t1 = begin_transaction('t1', isolation_level=1)
t2 = begin_transaction('t2', isolation_level=1)

t1.insert(1)
t2.select()
t1.commit()
t2.select()
t2.close()
