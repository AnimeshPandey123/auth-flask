from flask import Flask,request
from auth import *

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!!'

@app.route('/login', methods=[ 'POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	authenticate = auth(email, password)
	return authenticate.login()

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)