import flask
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.wrappers.response import Response


from db.models import User
from webapp.forms import LoginForm
from webapp.tasks_table_filler import aggregate_profile_table_data


@login_required
def user_profile() -> str:
    profile_table = aggregate_profile_table_data(current_user.id)
    return flask.render_template('tasks_catalog.html', title='Your tasks', table=profile_table)


def user_sign_in() -> str | Response:
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('.user_profile'))
    login_form = LoginForm()
    return flask.render_template('form.html', title='Sign in', form=login_form)


def process_login() -> Response:
    if flask.request.method != 'POST':
        return flask.redirect(flask.url_for('.user_sign_in'))
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('.user_profile'))
    form = LoginForm()
    if not form.validate_on_submit():
        flask.flash(*form.email.errors)
        return flask.redirect(flask.url_for('.user_sign_in'))
    user = User.find_user_by_email(flask.request.form.get('email'))
    if user and user.check_password(flask.request.form.get('password')):
        login_user(user)
        return flask.redirect(flask.url_for('.user_profile'))
    flask.flash('Wrong e-mail or password')
    return flask.redirect(flask.url_for('.user_sign_in'))


@login_required
def process_logout() -> Response:
    logout_user()
    return flask.redirect(flask.url_for('.user_sign_in'))
