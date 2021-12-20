Upewniamy się, że jesteśmy w naszym wirtualnym środowisku (po lewej stronie w terminalu powinno się wyświetlać (env)), że jesteśmy w folderze `7.indexes`, i że Postgres jest uruchomiony:

```
sudo service postgresql start
```

Tworzymy tabele (`users` i `presents`):
```
python3 1.createtables.py
```

Dodajemy 10 000 użytkowników, każdy kupuje prezent losowemu użytkownikowi (to może potrwać parę sekund):
```
python3 2.addusers.py
```

Wyświetlamy 10 osób, które otrzymają najwięcej prezentów i mierzymy, ile czasu to zajmie (może zająć kilka sekund):
```
time python3 3.lucky.py
```

Dodajemy indeks na kolumnie "user_to" w tabeli "presents":
```
time python3 4.addindex.py
```

I próbujemy jeszcze raz, powinno zadziałać dużo, dużo szybciej:
```
time python3 3.lucky.py
```