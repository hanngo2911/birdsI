#
# auth.py
# This file contains the class definitions needed for a user to register
# and login
#

import bcrypt

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

	def valid_email(email, email_repeat):
		pass

	def valid_password(password, password_repeat):
		pass


