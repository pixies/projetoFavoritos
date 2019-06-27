from flask import render_template, flash, redirect, url_for
from core.config import app, bcrypt, db
from core.user_form import UserRegisterForm
from core.models import User

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    # TODO make register
    form = UserRegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Hi, {form.username.data} your account has been created! You are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login')
def login():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('about.html')