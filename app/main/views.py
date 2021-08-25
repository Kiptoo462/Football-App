from flask import Blueprint, request, render_template,redirect,url_for,abort
from flask_login import login_required
from . import main
from app import db
from ..models import User, Competition
import urllib.request
from ..request import get_competition


@main.route('/')
def index():
    all_competitions = get_competition()

    title="Home"

    return render_template('index.html',title=title, all_competitions=all_competitions)


@main.route('/home')
@login_required
def homepage():
  
    title="Homepage"

    return render_template('home.html',title=title)