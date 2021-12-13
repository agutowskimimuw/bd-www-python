from flask import Flask, render_template
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
