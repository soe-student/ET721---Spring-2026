from flask import Flask, render_template, request, redirect, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"   # needed for login session

# connect DB
def get_db():
    conn = sqlite3.connect("flask_auth.db")
    conn.row_factory = sqlite3.Row
    return conn

# HOME → login
@app.route("/")
def home():
    return render_template("login.html")

# SIGNUP PAGE
@app.route("/signup")
def signup():
    return render_template("signup.html")

# HANDLE SIGNUP
@app.route("/signup", methods=["POST"])
def signup_post():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM users WHERE username=? OR email=?",
            (username, email)
        )
        existing_user = cursor.fetchone()
        if existing_user:
            flash("Username or Email already exists")
            return redirect("/signup")
    except Exception as e:
        flash("An error occurred. Please try again.")
        return redirect("/signup")

    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, password)
    )
    conn.commit()
    conn.close()

    return redirect("/")

# LOGIN Routing
@app.route("/login", methods=["POST"])
def login():
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
    app.run(debug=True)