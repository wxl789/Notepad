from flask_login import UserMixin
from flask_wtf import FlaskForm as Form
from werkzeug.security import check_password_hash, generate_password_hash
from  wtforms import  StringField,PasswordField
from wtforms.validators import DataRequired

from App.exp import db

class User(db.Model,UserMixin):

    __tablename__ = 'User'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False,
    )

    phone = db.Column(
        db.String(13),
        unique=True,
    )

    email = db.Column(
        db.String(120),
        unique=True,
    )

    password_hash = db.Column(
        db.String(256),
        nullable=False,
    )

    @property
    def password(self):
        return AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,pwd):
        if check_password_hash(self.password_hash,pwd) :
            return True
        else:
            return False

    def __repr__(self):
        return '<User %s>' % self.username

