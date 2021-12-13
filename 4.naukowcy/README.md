Upewniamy się, że jesteśmy w naszym wirtualnym środowisku (po lewej stronie w terminalu powinno się wyświetlać (env)) i że jesteśmy w folderze `4.naukowcy`.

Tworzymy bazę danych:
```
python3 create_db.py
```

I uruchamiamy aplikację:
```
export FLASK_APP=naukowcy
export FLASK_ENV=development
flask run
```

Teraz wchodzimy w przeglądarce na stronę http://localhost:5000.

Zadanie: dokończ aplikację - na stronie http://localhost:5000/doktoranci/4 chcemy zobaczyć wszystkich doktorantów osoby o ID 4 (tzn. wszystkich, którzy mają tę osobę wpisaną jako promotora).
