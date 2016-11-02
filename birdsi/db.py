#
# db.py
# This files contains all of the methods to query the database
#

import sqlite3 as sql

def insertUser(email, username,hashed_password):
    con = sql.connect("birdsi.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,email, password) VALUES (?,?,?)", \
        (username,email,hashed_password))
    con.commit()
    con.close()

def retrieveUser(email):
    con = sql.connect("birdsi.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE email = (?)", (email,))
    users = cur.fetchall()
    con.close()
    return (users[0] if users else None)

def retrieveUsers():
    con = sql.connect("birdsi.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    con.close()
    return users

