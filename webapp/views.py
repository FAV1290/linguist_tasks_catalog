import flask
from flask_login import login_required, login_user, logout_user
from werkzeug.wrappers.response import Response


from db.models import User
from backend.users_manager import check_user_password
from webapp.forms import LoginForm


@login_required
def user_profile() -> str:
    return flask.render_template('tasks_catalog.html', title='Your profile')


def user_sign_in() -> str:
    login_form = LoginForm()
    return flask.render_template('form.html', title='Sign in', form=login_form)


def process_login() -> Response:
    form = LoginForm()
    if not form.validate_on_submit():
        flask.flash(*form.email.errors)
        return flask.redirect(flask.url_for('.user_sign_in'))
    user = User.find_user_by_email(flask.request.form.get('email'))
    if user and check_user_password(user, flask.request.form.get('password')):
        login_user(user)
        return flask.redirect(flask.url_for('.user_profile'))
    flask.flash('Wrong e-mail or password')
    return flask.redirect(flask.url_for('.user_sign_in'))


@login_required
def process_logout() -> Response:
    logout_user()
    return flask.redirect(flask.url_for('.user_sign_in'))
