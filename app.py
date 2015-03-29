import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# DB configuration
DATABASE = '/Users/ardian/code/flaskblog/'
DEBUG = True
SECRET_KEY = 'Jukthauthasdhasjdj!!>AAAzzza'
USERNAME = 'admin'
PASSWORD = 'admin'

# Application code

app = Flask(__name__)
app.config.from_object(__name__)

# DB connection

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])


if __name__ == '__main__':
    app.run()