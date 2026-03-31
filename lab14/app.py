"""
Soe Kaythi
Lab 14, mini blog app using Flask
March 19, 2026
"""

from flask import Flask,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# database connection
db = mysql.connector.connect(
    host="localhost",
    user="flaskuser",
    password="password123",
    database="blogDB"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_blog')
def add_blog():
    username = request.form['username']
    email = request.form['email']
    title = request.form['title']
    content = request.form['content']

    #insert into table blogs
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)",(username, email))
    db.commit()
    #get the id of the last row that was inserted into the database and store it in user_id
    user_id = cursor.lastrowid

    #insert into table blogs
    cursor.execute("INSERT INTO blogs (user_id, title, content) VALUES (%s, %s, %s)",(user_id, title, content))
    db.commit()

    cursor.close()

    return redirect(url_for('/blogs'))

@app.route('/blogs')
def blogs():
    cursor = db.cursor()
    cursor.execute("SELECT blogs.id, blogs.title, blogs.content, users.username, users.email FROM blogs JOIN users ON blogs.user_id = users.id")
    # Fetch all the data
    data = cursor.fetchall()
    cursor.close()
    return render_template('blogs.html', posts=data)

if __name__ == '__main__':
    app.run(debug=True)
