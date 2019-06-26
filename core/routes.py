from flask import render_template
from core.config import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('about.html')