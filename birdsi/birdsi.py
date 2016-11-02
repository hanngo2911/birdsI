from flask import Flask, session, redirect, request, url_for, \
	render_template, g
from auth import UserManager as UserManager
from sqlite3 import dbapi2 as sqlite3

app = Flask(__name__)

### App Config ###
app.config.update(dict(
	DATABASE="birdsi.db",
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))

"""
### DB Config ###

Adapted from 
https://github.com/pallets/flask/blob/master/examples/flaskr/flaskr/flaskr.py
and
http://flask.pocoo.org/docs/0.11/patterns/sqlite3/
"""

def connect_db():
	"""Connects to database given in config"""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

def get_db():
	"""Opens new database connection if it is not already open"""
	with app.app_context():
		if not hasattr(g, 'sqlite_db'):
			g.sqlite_db = connect_db()
		return g.sqlite_db

def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_db(error):
	"""Closes the database when request is closed"""
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

### Routing ### 
@app.route('/')
def index():
	if session.get('uid'):
		return 'Hello, World!'

	return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		# User has submitted the login form
		email = request.form['email']
		password = request.form['password']
		if UserManager.login(email, password):
			return redirect(url_for('index'))
		# Authentication Failed
		error = "Invalid email or password"
		return render_template('login', error = error)

	# User is visiting the login page, and has not submitted
	return render_template('login', error = error)

@app.route('/register', methods = ['GET', 'POST'])
def register():
	error = None;
	if request.method == 'POST':
		# User has submitted the registration form
		name = request.form['name']
		email = request.form['email']
		email_repeat = request.form['email_repeat']
		password = request.form['password']
		password_repeat = request.form['password_repeat']
		if UserManager.register(name, email, email_repeat, password,
			password_repeat):
			return redirect(url_for('index'))

		# Registration Failed
		error = "Registration failed, please try again"
		return render_template('registration', error = error)

	# User is visiting the registration page, and has not submitted
	return render_template('registration', error = error)

		


if __name__ == '__main__':
	app.run()