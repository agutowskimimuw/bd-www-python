Upewniamy się, że jesteśmy w naszym wirtualnym środowisku (po lewej stronie w terminalu powinno się wyświetlać (env)) i że jesteśmy w folderze `3.flask.db.render`.

Tworzymy bazę danych:
```
python3 create_db.py
```

I uruchamiamy aplikację:
```
export FLASK_APP=things
export FLASK_ENV=development
flask run
```

Teraz wchodzimy w przeglądarce na stronę http://localhost:5000.
