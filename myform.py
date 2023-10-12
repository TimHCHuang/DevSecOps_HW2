import flask
from flask import Flask, render_template, request
from werkzeug.security import check_password_hash


def check_password(passwordhash, password):
    return check_password_hash(passwordhash, password)
    
app = flask.Flask(__name__)

def getHash():
	with open('myhash.txt', 'r') as f:
		myhash = f.read().strip()
		return myhash

@app.route("/myform")
def form():
    return render_template('myform.html')
@app.route("/submit", methods=['POST'])
def submit():
    account = request.values['account']
    password = request.values['password']
    try:
    	assert check_password(getHash(), password)
    except AssertionError:
        return "<H1> Error Account or Password! <H1>"
    return render_template('resp.html', **locals())

if __name__ == '__main__':
    app.run()
