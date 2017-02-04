from flask import Flask
from flask_hooker import hooker


def return_name(json):
    print json['name']


app = Flask(__name__)
hooker = hooker.Hooker(app, url_prefix='/hook')

hooker.add_handler('name', return_name, 'X-Custom-Event')


@app.route('/')
def index():
    return 'index'
