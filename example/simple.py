from flask import Flask
from flask_hooker import Hooker


def print_name(json):
    print 'print_name: new request from:', json['username']

app = Flask(__name__)

hooker = Hooker(app=app, url_prefix='/webhook')

hooker.add_handler(event='name', func=print_name, event_type='X-Custom-Event')


@app.route('/')
def index():
    return '<h> Flask-Hooker </>'


if __name__ == '__main__':
    app.run(debug=True)
