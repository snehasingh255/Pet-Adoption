from flask import Flask,render_template, request,session
import subprocess
from flask import redirect, url_for 
#from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Adoption.html")  

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    os.system("python loginpage.py")
    return "Script executed!"

@app.route('/cat')
def cat():
    return render_template('cat.html')

@app.route('/dog')
def dog():
    return render_template('dog.html')

@app.before_request
def set_logged_user():
    username = os.environ.get("LOGGED_IN_USER")
    if username:
        session["loggedInUser"] = username

def on_successful_login(username):
    os.environ["LOGGED_IN_USER"] = username
    subprocess.Popen(["python", "app.py"], env=os.environ)


if __name__ == '__main__':
    app.run(debug=True)
