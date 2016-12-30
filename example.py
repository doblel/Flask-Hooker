from flask import Flask
from flask_hooker.hooker import Hooker



def github_push(json):
    print json

app = Flask(__name__)

hooker = Hooker(app=app, url_prefix='/hook')

hooker.add_handler(event='push', func=github_push, event_type='X-Github-Event')


@app.route('/')
def index():
    return '<h> Flask-Hooker </>'


if __name__ == '__main__':
    app.run(debug=True)


# $curl -H "Content-Type:application/json" -H "X-Custom-Event:name" -d '{"username":"doblel"}' -X POST localhost:5000/hook