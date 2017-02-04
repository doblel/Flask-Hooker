"""example.py."""
from flask import Flask
from flask_hooker.hooker import Hooker


def print_username(json):
    """Print name."""
    print('username: %s' % json['username'])


app = Flask(__name__)

hooker = Hooker(app=app, url_prefix='/webhook')

hooker.add_handler(event='name', func=print_username, event_type='X-Custom-Event')


@app.route('/')
def index():
    """Index view of your app."""
    return '<h> Flask-Hooker </>'


if __name__ == '__main__':
    app.run(debug=True, host='138.0.184.1', port=3000)

# $curl -H "Content-Type:application/json" -H "X-Custom-Event:name" -d '{"username":"doblel"}' -X POST localhost:5000/webhook
