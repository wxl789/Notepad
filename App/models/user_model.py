from flask_login import UserMixin
from flask_wtf import FlaskForm as Form
from  wtforms import  StringField,PasswordField
from wtforms.validators import DataRequired

from App.exp import db

class LoginForm(Form):
    accountNumber = StringField('accountNumber',validators=[DataRequired('accountNumber is null')])
    password = PasswordField('password', validators=[DataRequired('password is null')])

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

    email = db.Column(
        db.String(120),
    )

    password = db.Column(
        db.String(32),
        nullable=False,
    )

    avatar_hash = db.Column(
        db.String(32)
    )

    def checkUser(self,name,pwd):
        if self.username == name and self.password == pwd:
            return True
        else:
            return False

    def __repr__(self):
        return '<User %s>' % self.username

