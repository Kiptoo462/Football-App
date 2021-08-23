from flask import Blueprint, render_template, flash, redirect, request, url_for, abort
from flask_login import login_required, login_user, logout_user,current_user
from .. import main
from app import db


from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm, UpdateProfile
from ..email import welcome_message

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()

    if form.validate_on_submit():

        user = User(
                    email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
                    
        db.session.add(user)
        db.session.commit()
        welcome_message("Welcome to the Global Football community.","email/welcome",user.email,user=user)

        return redirect(url_for('auth.login'))

    title = "Sign Up"
    return render_template('auth/signup.html', RegistrationForm=form, title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.passwordVerification(
                form.password.data):
            login_user(user,form.remember.data)

            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Authentication Failed!')

    title = "Login"
    return render_template('auth/login.html', LoginForm=form, title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('main.index'))


@auth.route('/profile', methods = ['POST','GET'])
@login_required
def profile():
    user = current_user
    user_id = current_user._get_current_object().id

    if user is None:
        abort(404)

    title = "Profile"

    return render_template('auth/profile.html', title=title, user=user)


@auth.route('/profile/update',methods = ['GET','POST'])
@login_required
def update_profile():
    user = current_user

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.favourite_team = form.favourite_team.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.profile',))

    return render_template('auth/update.html',form =form)