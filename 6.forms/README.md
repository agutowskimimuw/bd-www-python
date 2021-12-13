Upewniamy się, że jesteśmy w naszym wirtualnym środowisku (po lewej stronie w terminalu powinno się wyświetlać (env)) i że jesteśmy w folderze `6.forms`.

Tworzymy bazę danych:
```
python3 create_db.py
```

I uruchamiamy aplikację:
```
export FLASK_APP=forms
export FLASK_ENV=development
flask run
```

Teraz wchodzimy w przeglądarce na stronę http://localhost:5000.
