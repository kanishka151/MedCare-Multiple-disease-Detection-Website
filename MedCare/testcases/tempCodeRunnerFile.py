
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import pandas as pd
import pickle
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#file_path = 'testcases\diabetes-prediction-rfc-model.pkl'
#with open(file_path, 'rb') as file:
    # Load the object from the file
#    classifier = pickle.load(file)

file_path_diabetes = ('testcases\diabetes_model.sav')
classifier = pickle.load(open(file_path_diabetes, 'rb'))
file_path_cancer = ('testcases\cancer.pkl')
model = pickle.load(open(file_path_cancer, 'rb'))
#model1 = pickle.load(open('model1.pkl', 'rb'))

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# bootstrap = Bootstrap(app)
# db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))