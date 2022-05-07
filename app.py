#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
    return 'Hello'

if __name__ == '__main__':
    app.run('0.0.0.0', port=5010, debug=True)
