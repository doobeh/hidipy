import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = 'SECRET_KEY'
SITE_NAME = 'HIDiPy'
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite3'
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

PAGINATION_SIZE = 20
SECURITY_USER_IDENTITY_ATTRIBUTES = 'username'

try:
    from user_config import *
except ImportError:
    pass  # log using defaults.