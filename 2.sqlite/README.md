Zanim skonfigurujemy Postgresa, zobaczmy, jak w ogóle wygląda praca z bazą danych na przykładzie SQLite (bardzo prosta baza danych, zapisywana w jednym pliku).

Upewniamy się, że jesteśmy w naszym wirtualnym środowisku (po lewej stronie w terminalu powinno się wyświetlać (env)) i że jesteśmy w folderze `2.sqlite`. Wpisujemy:

```
python3 create_db.py
```

Powinien zostać stworzony plik `db.sqlite3`. Uruchamiamy:

```
python3 use_db.py
```

Powinniśmy zobaczyć zawartość naszej bazy.
