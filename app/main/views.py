from flask import Blueprint, request, render_template,redirect,url_for,abort
from flask_login import login_required, current_user
from . import main
from app import db
from ..models import User,Country
import urllib.request
from ..request import getTeam
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required


@main.route('/home')
@main.route('/')
def index():
    team = getTeam()

    title="Home"

    return render_template('index.html',title=title, team=team)