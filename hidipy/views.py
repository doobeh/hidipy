from flask import Blueprint, current_app as app, url_for, jsonify
from flask import render_template, abort, redirect, request
from hidipy.models import User, db
from flask_security import login_required, current_user
from datetime import datetime, timedelta, date
from sqlalchemy import func
from jinja2.exceptions import TemplateNotFound
import random


mod = Blueprint('core', __name__)


@mod.route('/<page>.door')
def generic(page):
    try:
        return render_template('generic/{}.html'.format(page))
    except TemplateNotFound:
        abort(404)


@mod.route('/')
def home():
    return render_template('home.html')
