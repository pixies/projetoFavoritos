from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = '3d6f4f03510e6f6f606f9b6cf8ae1f8da81dc1766f01c15c31ec008a022edc20'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'

#Database object
db = SQLAlchemy(app)

#bcrypt object
bcrypt = Bcrypt(app)

#LoginManager object
login_manager = LoginManager(app)

from core import routes