from flask import Flask, render_template, request, redirect, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "1234"


# connect DB
def get_db():
    conn = sqlite3.connect("flask_auth.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT    UNIQUE NOT NULL,
            email    TEXT    UNIQUE NOT NULL,
            password TEXT    NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# HOME → login
@app.route("/")
def home():
    return render_template("login.html")


# LOGIN PAGE (GET) + HANDLE LOGIN (POST)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    ).fetchone()
    conn.close()

    if user:
        session["user"] = username
        return redirect("/dashboard")
    else:
        flash("Invalid Email or Password")
        return redirect("/")


# SIGNUP PAGE
@app.route("/signup")
def signup():
    return render_template("signup.html")


# HANDLE SIGNUP
@app.route("/signup", methods=["POST"])
def signup_post():
    username = request.form["username"]
    email    = request.form["email"]
    password = request.form["password"]

    conn   = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? OR email=?",
        (username, email)
    )
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        flash("Username or Email already exists")
        return redirect("/signup")

    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, password)
    )
    conn.commit()
    conn.close()

    return redirect("/")


# DASHBOARD
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect("/")


# LOGOUT
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)