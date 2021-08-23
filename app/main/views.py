from flask import Blueprint, request, render_template,redirect,url_for,abort
from flask_login import login_required
from .import main
from app import db


@main.route('/')
def index():
    title="Home"

    return render_template('index.html',title=title)

@main.route('/home')
@login_required
def homepage():
  
    title="Homepage"

    return render_template('home.html',title=title)