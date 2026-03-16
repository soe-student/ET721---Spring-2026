
"""
Lab 11, Introduction to Flask
March 10, 2026
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Prof.Wu"
    fruits = ["Apple", "Banana", "Cherry"]
    fruit = 'pineapple'
    return render_template('index.html', username=name, fruitslist=fruits, f=fruit)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/quotes')
def quotes():
    return render_template('quote.html')

if __name__ == '__main__':
    app.run(debug=True)