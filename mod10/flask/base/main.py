import flask

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>My First Flask Program!</h1>'
