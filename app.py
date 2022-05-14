#!/usr/bin/python3

from flask import Flask, render_template, request, url_for, redirect
import sqlite3

DB_PATH = '/tmp/test.s3db'

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_item():
    # Fetch and validate input data
    a = request.form.get('a')
    b = request.form.get('b')
    if a is None or b is None:
        abort(400)
    try:
        a = int(a)
    except ValueError:
        abort(400)
    # Try to insert a new entry:
    with sqlite3.conect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO t1(a, b) VALUES (?, ?)', (a, b))
        conn.commit()
        # Tell user to load main page again
    return redirect(url_for('main_page'))  
      
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
