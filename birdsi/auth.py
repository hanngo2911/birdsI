#
# auth.py
# This file contains the class definitions needed for a user to register
# and login
#

import bcrypt
import re

class User():
	"""
	Definition of a User
	
	Accepted kwargs:
	- uid (userid)
	- email
	- name (company name)
	- password (unhashed)
	"""
	def __init__(self, **kwargs):
		for attr, value in kwargs:
			self.__setattr__(attr, value)

	


class UserManager:
	"""Handles user registration, and authentication"""

	def valid_email(email, email_repeat):
		# Checks if emails match and for regex match
		if email == email_repeat \
			and re.match("^[a-zA-Z0-9.-]+@[a-zA-Z0-9.]+\\.[a-zA-Z0-9]+$", email):
			return True
		
		return False			

	def valid_password(password, password_repeat):
		# Checks if passwords match, longer than 6 chars, contains uppercase 
		# and lower case letter, a number, and a special character/number
		if password == password_repeat \
			and len(password) > 6 \
			and re.match("[a-z]", password) \
			and re.match("[A-Z]", password) \
			and re.match(r"[0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
			return True

		return False 
		
	def register(name, email, email_repeat, password, password_repeat):
		# This method requires the user to enter email and password twice
		# to ensure correctness. 
		#
		# Returns True if successful, False otherwise
		# 
		# Currently, no validation email is being sent to the given email
		
		if valid_email(email, email_repeat) \
			and valid_password(password, password_repeat) \
			and name:
			# Email valid, password valid, name exists, good to go
			password_bytes = password.tobytes()
			hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

			# Ready to store in DB
			
		return False

	def login(email, password):
		# Returns True if successful, False if not
		# 

		# Query DB for user attempting to log in
		user = query_db('SELECT * FROM users WHERE email = ?',	
			[email], one=True)
		
		# Need to check if user is returned (email exists) and password
		# matches the one stored for that user
		if user is not None and \
			bcrypt.hashpw(password, user['password']) == user['password']:
			
			# User's credentials match, can set session and return True
			Session['name'] = user['name'];
			return True

		return False

	def logout():
		if 'name' in session:
			session.pop('name', None)
			