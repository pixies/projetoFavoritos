from flask import render_template, flash, redirect, url_for
from core.config import app, bcrypt, db
from flask_login import login_user, current_user, logout_user
from core.user_form import UserRegisterForm, UserLoginForm
from core.models import User



@app.route('/')
@app.route('/home')
def home():
    #user = current_user
    #return render_template('home.html')
    return redirect(url_for('favorites'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserRegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Hi, {form.username.data} your account has been created! You are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('favorites'))
        else:
            flash(f'Login unsuccessfull. Please check email end password', 'danger')
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/blog')
def blog():
    return render_template('about.html')



