from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/ping')
def ping():
	return "PONG"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)