from flask import Flask, render_template, request, session, redirect, url_for,flash
import mysql.connector
import subprocess
import os
from werkzeug.security import generate_password_hash, check_password_hash
import db

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'singh@sneha25',
    'database': 'petAdoption'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route("/")
def home():
    return render_template("Adoption.html")

@app.route("/admin")
def admin():
    if session.get("role") != "admin":
        flash("Access denied: Admins only", "error")
        return redirect(url_for("login"))
    return render_template("admindashboard.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/cat")
def cat():
    return render_template("cat.html")

@app.route("/dog")
def dog():
    return render_template("dog.html")

@app.before_request
def set_logged_user():
    username = os.environ.get("LOGGED_IN_USER")
    if username:
        session["loggedInUser"] = username

app.secret_key = 'adoptwebsite2525'

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = db.get_user_by_username(username)
        if user and check_password_hash(user["password"], password):
            session["loggedInUser"] = user["username"]
            session["role"] = user.get("role", "user") 
            flash(f"Welcome back, {username}!", "success")

            # Redirect based on role
            if user.get("role") == "admin":
                return redirect(url_for("admin"))
            else:
                return redirect(url_for("home"))
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for("login"))
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("Passwords do not match", "error")
            return redirect(url_for("register"))

        hashed_pw = generate_password_hash(password)
        db.insert_user(username, email, hashed_pw)
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route('/resetpass', methods=['GET', 'POST'])
def resetpass():
    if request.method == 'POST':
        email = request.form['email']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('resetpass'))

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            hashed_pw = generate_password_hash(new_password)
            cursor.execute("UPDATE users SET password = %s WHERE email = %s", (hashed_pw, email))
            conn.commit()
            flash('Password reset successful!', 'message')
            cursor.close()
            conn.close()
            return redirect(url_for('login'))
        else:
            flash('Email not found', 'error')
            cursor.close()
            conn.close()
            return redirect(url_for('resetpass'))
    return render_template("resetpass.html")

if __name__ == '__main__':
    app.run(debug=True)