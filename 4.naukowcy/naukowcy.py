from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def show_researchers():
    con = sqlite3.connect('db.sqlite3')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("SELECT * FROM naukowiec")
    rows = cur.fetchall()

    cur.close()
    con.close()

    return render_template('naukowcy.html', naukowcy=rows)


@app.route("/doktoranci/<int:student_id>")
def show_students(student_id):
    return 'TODO: zaimplementować tę funkcję...'
