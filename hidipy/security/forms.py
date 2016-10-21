from flask_security import LoginForm
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField


class AppLoginForm(LoginForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])