from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'hi everyone. this is my first web app'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
