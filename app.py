from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f;lkah3oiehg'

@app.route('/')
def index():
    return '<h1>This page is functional</h1>'

if __name__ == '__main__':
    app.run(debug=True)