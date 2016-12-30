#Flask-Hooker

###Simple usage
```python 
from flask import Flask
from flask_hooker import Hooker

def github_issue(json):
    print 'new issue at:', json['issue']['url]

app = Flask(__name__)

hooker = Hooker(app=app, url_prefix='/hook')

# with fabrics
# hooker = Hooker()
# hooker.init_app(app)

hooker.add_handler(event='issues', func=github_issue, event_type='X-Github-Event')

...
```
