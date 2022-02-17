from flask import flash, render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from app.auth import auth
from app.main.forms import LoginForm,SignupForm
from app.models import User
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if (User.username == login_form.username.data):
            login_user(user, remember=login_form.remember.data)
            return redirect(url_for('main.home'))
        else:
            flash('Invalid login details')
    title = "User login"
    return render_template('/login.html', login_form=login_form, title=title)


@auth.route('/signup', methods=["GET", "POST"])
def sign_up():
    form = SignupForm()
    get_user = User.query.filter_by(username=form.username.data).first()
    if get_user:
        flash("The username already exists!")

    else:

        if form.validate_on_submit():
            user = User(username=form.username.data,
                         email=form.email.data)
            db.session.add(user)
            db.session.commit()

            flash('Account has been created successfully')

            return redirect(url_for('auth.login'))

    return render_template('/signup.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
