"""
    squarker.core
    ~~~~~~~~~~~~~
    the gears to get the machine turning.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from hidipy.models import User, Role
from datetime import datetime

def create_app(config_filename):
    factory_app = Flask(__name__)
    factory_app.config.from_pyfile(config_filename)
    return factory_app

app = create_app('../config.py')

# We use this to ease our pagination work.
app.jinja_env.add_extension('jinja2.ext.do')

from hidipy.views import mod
app.register_blueprint(mod)

#: Flask-SQLAlchemy extension instance
db = SQLAlchemy()
db.init_app(app)

# Setup Flask-Security
user_store = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_store)


# Context:
@app.context_processor
def inject_data():
    return {
        'now': datetime.now()
    }