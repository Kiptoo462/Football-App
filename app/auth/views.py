from flask import render_template, flash, redirect, request, url_for
from flask_login import login_required, login_user, logout_user,current_user


from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db

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
        return redirect(url_for('auth.login'))

    title = "Sign Up"
    return render_template('auth/signup.html', form=form, title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.passwordVerification(
                login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Authentication Failed!')
    title = "Login"
    return render_template('auth/login.html',
                           login_form=loginform,
                           title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/profile')
@login_required
def profile():
    
    title = "Profile"

    return render_template('auth/profile.html', title=title)