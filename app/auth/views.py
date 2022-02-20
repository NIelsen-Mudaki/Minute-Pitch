from flask import flash, render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from . import auth
from app.main.forms import LoginForm,SignupForm
from app.models import User
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is not None and user.check_password(login_form.password.data):
            login_user(user)
            return redirect(request.args.get("next") or url_for("main.index"))
        else:
            flash('Invalid login details')
    title = "User login"
    return render_template('auth/login.html', login_form=login_form, title=title)


@auth.route('/signup', methods=["GET", "POST"])
def sign_up():
    form = SignupForm()
    if form.validate_on_submit():
        password=form.password.data
        user = User(username=form.username.data,
                    email=form.email.data)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash('Account has been created successfully')

        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/tests')
def test():
    return 'Hello'
