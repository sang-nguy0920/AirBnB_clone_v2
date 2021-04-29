#!/usr/bin/python3
"""
A script that starts a Flask web application.
"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world(strict_slashes=False):
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb(strict_slashes=False):
    return 'HBNB'


@app.route('/c/<path:subpath>')
def hello_c(subpath, strict_slashes=False):
    return 'C {}'.format(subpath.replace('_', ' '))

app.run(host='0.0.0.0')
