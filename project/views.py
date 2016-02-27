from flask import render_template
from project import app

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login/")
def login():
    return render_template('login.html')
