#!/usr/bin/python3
"""
A script that starts a Flask web application.
"""


from flask import Flask
from flask import render_template
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


@app.route('/python/<path:subpath>')
def hello_pythonpath(subpath, strict_slashes=False):
    return 'Python {}'.format(subpath.replace('_', ' '))


@app.route('/python/')
def hello_pythonnopath(strict_slashes=False):
    return 'Python is cool'


@app.route('/number/<int:number>')
def hello_number(number, strict_slashes=False):
    return '{} is a number'.format(number)


@app.route('/number_template/<int:number>')
def hello_numbertemp(number, strict_slashes=False):
    return render_template('5-number.html', number=number)

app.run(host='0.0.0.0')
