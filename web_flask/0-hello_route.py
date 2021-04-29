#!/usr/bin/python3
"""
A script that starts a Flask web application.
"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world(strict_slashes=False):
    return 'Hello HBNB!'

app.run(host='0.0.0.0')
