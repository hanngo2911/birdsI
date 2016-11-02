from flask import Flask, session, redirect, request, url_for, \
	render_template, g
import auth


app = Flask(__name__)
UserManager = auth.UserManager()

### App Config ###
app.config.update(dict(
	DATABASE="birdsi.db",
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))

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
		return render_template('login.html', error = error)

	# User is visiting the login page, and has not submitted
	return render_template('login.html', error = error)

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
		return render_template('registration.html', error = error)

	# User is visiting the registration page, and has not submitted
	return render_template('registration.html', error = error)

		


if __name__ == '__main__':
	app.run()