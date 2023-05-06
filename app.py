from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/')
def index():
    return 'BOTTY SERVER'


if __name__ == '__main__':
    app.run()
