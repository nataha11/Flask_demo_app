#!/usr/bin/python3

from flask import Flask, render_template
import sqlite3

DB_PATH = '/tmp/test.s3db'

app = Flask(__name__)

@app.route('/')
def main_page():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM t1')
    return render_template(
        'main_page.html',
        columns=[x[0] for x in cur.description],
        data=cur.fetchall()
     )

if __name__ == '__main__':
    app.run('0.0.0.0', port=5010, debug=True)
