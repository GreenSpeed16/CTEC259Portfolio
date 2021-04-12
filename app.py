from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f;lkah3oiehg'

if __name__ == '__main__':
    app.run(debug=True)