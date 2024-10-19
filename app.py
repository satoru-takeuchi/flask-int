from flask import FLask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'
