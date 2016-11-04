from flask import Flask, session, redirect, request, url_for, \
	render_template, g
from sqlite3 import dbapi2 as sqlite3