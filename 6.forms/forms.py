from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def show_things():
    con = sqlite3.connect('db.sqlite3')
    con.row_factory = sqlite3.Row   # dzięki temu będziemy się mogli odwoływać do row.nazwa_kolumny, a nie tylko row[0]
    cur = con.cursor()

    cur.execute("SELECT * FROM things")
    rows = cur.fetchall()

    cur.close()
    con.close()

    return render_template('things.html', things=rows)


@app.route("/add_thing")
def add_thing():
    thing_id = request.args['id']
    thing_name = request.args['name']

    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    # Znaki zapytania poniżej są specyficzne dla SQLite, w Postgresie wygląda to inaczej.
    # Czemu wolimy Postgresa od SQLite? Spróbuj wpisać (w przeglądarce) dowolny napis jako thing_id.
    cur.execute("INSERT INTO things VALUES (?, ?)", (thing_id, thing_name))

    con.commit()
    cur.close()
    con.close()

    # Wyświetlanie komunikatu w ten sposób nie jest zbyt wygodne dla użytkownika.
    # Żeby to zrobić lepiej, można użyć "redirect" z Flaska, albo nawet "flash":
    # https://flask.palletsprojects.com/en/2.0.x/patterns/flashing/
    return 'Pomyślnie dodano rzecz do bazy!<br><a href="/">Wróć do strony głównej</a>'
