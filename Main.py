from flask import Flask

app = Flask(__name__)


@app.route('/')

def hello_world():
    return 'Hello there Peta. Your Capstone Project team is doing an amazing job !'


if __name__ == '__main__':

    app.run(host="0.0.0.0")
