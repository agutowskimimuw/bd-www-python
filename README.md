Przed wszystkim upewnijmy się, że mamy zainstalowanego Pythona i venv:
```
sudo apt install python3 python3-venv
```

Żeby nie instalować bibliotek Pythona globalnie, w całym systemie, tworzymy "wirtualne środowisko":

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

W terminalu po lewej stronie powinniśmy widzieć napis (env), oznaczający, że jesteśmy w naszym wirtualnym środowisku.
Żeby z niego wyjść, wystarczy napisać `deactivate` (albo zamknąć okno terminala).

Wchodzimy do katalogu jednego z projektów (np. `cd 1.flask.hello`). W folderze projektu są instrukcje, jak go uruchomić.
