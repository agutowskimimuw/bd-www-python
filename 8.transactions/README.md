Upewniamy się, że jesteśmy w naszym wirtualnym środowisku (po lewej stronie w terminalu powinno się wyświetlać (env)), że jesteśmy w folderze `8.transactions`, i że Postgres jest uruchomiony:

```
sudo service postgresql start
```

Na studentsie trzeba zmodyfikować plik `transactions.py` - odkomentować linijkę w funkcji `connect` i uzupełnić login i hasło.

Czytamy kod źródłowy przykładów i je uruchamiamy:
```
python3 1.py
```

`transactions.py` dostarcza parę funkcji do prostego testowania transakcji (na tabeli z tylko jedną kolumną).
W przykładzie `4.py` można zobaczyć uruchamianie transakcji równolegle.
W przykładzie `5.py` powinien zostać rzucony wyjątek `SerializationFailure`, a w `7.py` wyjątek `DeadlockDetected`.
