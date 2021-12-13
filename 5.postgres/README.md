Jeśli już mamy zainstalowanego Postgresa, upewniamy się, że jest uruchomiony:
```
sudo service postgresql start
```

W przeciwnym przypadku instalujemy Postgresa.
```
sudo apt install postgresql
```

Stwórzmy użytkownika o nazwie takiej, jak nasz użytkownik w systemie, odpowiadającą bazę, i sprawdzamy, czy psql działa:
```console
albert@DESKTOP-RDAL0L1:~$ sudo -u postgres createuser --interactive
Enter name of role to add: albert
Shall the new role be a superuser? (y/n) y
albert@DESKTOP-RDAL0L1:~$ sudo -u postgres createdb albert
albert@DESKTOP-RDAL0L1:~$ psql
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1))
Type "help" for help.

albert=# \q
albert@DESKTOP-RDAL0L1:~$ 
```

Teraz stwórzmy osobnego użytkownika i bazę danych na potrzeby naszej aplikacji.
```
albert@DESKTOP-RDAL0L1:~$ psql
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1))
Type "help" for help.

albert=# CREATE USER flaskapp WITH ENCRYPTED PASSWORD 'Lt9wtCJbVyBFwGmz8Nxn';
CREATE ROLE
albert=# CREATE DATABASE flaskapp;
CREATE DATABASE
albert=# GRANT ALL PRIVILEGES ON DATABASE flaskapp TO flaskapp;
GRANT
albert=# \q
albert@DESKTOP-RDAL0L1:~$ 
```

Musimy jeszcze zmienić jeden plik konfiguracyjny (można użyć swojego ulubionego edytora zamiast vima):
```
sudo vim /etc/postgresql/12/main/pg_hba.conf
```
Znajdujemy linijkę (blisko końca pliku):
```
local   all             all                                     peer
```
I zamieniamy "peer" na "md5":
```
local   all             all                                     md5
```
Restartujemy postgresa:
```
sudo service postgresql restart
```

I zrobione! Teraz możemy uruchomić naszą aplikację.
Upewniamy się, że jesteśmy w naszym wirtualnym środowisku (po lewej stronie w terminalu powinno się wyświetlać (env)) i że jesteśmy w folderze `5.postgres`. Tworzymy tabelę w bazie danych:
```
python3 create_table.py
```
I z niej korzystamy:
```
python3 use_db.py
```
