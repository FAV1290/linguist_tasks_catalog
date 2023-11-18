import uuid
import flask
from werkzeug.wrappers.response import Response
from flask_login import login_required, login_user, logout_user, current_user


from db.models import User, Task
from webapp.table_fillers import (
    aggregate_tasks_table_data,
    aggregate_clients_table_data,
    aggregate_linguists_table_data,
    aggregate_tasktypes_table_data,
)
from db.converters import create_task_object
from webapp.forms import LoginForm, AddTaskForm
from db.changers import add_object, delete_object, update_task



@login_required
def user_profile() -> str:
    tasks_table = aggregate_tasks_table_data(current_user.id)
    return flask.render_template('tasks_catalog.html', title='Your tasks', table=tasks_table)


def user_sign_in() -> str | Response:
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('.user_profile'))
    return flask.render_template(
        'form.html',
        title='Sign in',
        form=LoginForm(),
        form_action=flask.url_for('.process_login'))


def process_login() -> Response:
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


@login_required
def add_task() -> str:
    add_task_form = AddTaskForm()
    add_task_form.define_choices(current_user.id)
    return flask.render_template(
        'form_with_header.html',
        title='Add new task',
        form=add_task_form,
        form_action=flask.url_for('.process_task_add'),
    )


@login_required
def process_task_add() -> Response:
    form = AddTaskForm()
    form.define_choices(current_user.id)
    if not form.validate_on_submit():
        for error in form.errors.values():
            flask.flash(*error)
        return flask.redirect(flask.url_for('.add_task'))
    new_task = create_task_object(current_user.id, flask.request.form)
    add_object(new_task)
    return flask.redirect(flask.url_for('.user_profile'))


@login_required
def delete_task(task_id: str) -> str:
    return flask.render_template('delete_confirmation.html', title='Delete task', task_id=task_id)


@login_required
def process_task_delete(task_id: str) -> Response:
    owner_is_valid, target_task = Task.validate_owner(uuid.UUID(task_id), current_user.id)
    if owner_is_valid and target_task:
        delete_object(target_task)
    return flask.redirect(flask.url_for('.user_profile'))


@login_required
def edit_task(task_id: str) -> str | Response:
    owner_is_valid, target_task = Task.validate_owner(uuid.UUID(task_id), current_user.id)
    if owner_is_valid and target_task:
        edit_task_form = AddTaskForm()
        edit_task_form.define_choices(current_user.id)
        edit_task_form.fill_with_task_data(target_task)
        form_action = flask.url_for('.process_task_edit', task_id=task_id)
        return flask.render_template(
            'form_with_header.html',
            title='Edit task',
            form=edit_task_form,
            form_action=form_action
        )
    return flask.redirect(flask.url_for('.user_profile'))


@login_required
def process_task_edit(task_id: str) -> Response:
    form = AddTaskForm()
    form.define_choices(current_user.id)
    if not form.validate_on_submit():
        for error in form.errors.values():
            flask.flash(*error)
        return flask.redirect(flask.url_for('.edit_task', task_id=task_id))
    update_task(current_user.id, uuid.UUID(task_id), flask.request.form)
    return flask.redirect(flask.url_for('.user_profile'))


@login_required
def user_settings() -> str:
    clients_table = aggregate_clients_table_data(current_user.id)
    linguists_table = aggregate_linguists_table_data(current_user.id)
    tasktypes_table = aggregate_tasktypes_table_data(current_user.id)
    return flask.render_template(
        'settings.html',
        title='Your Settings',
        clients_table=clients_table,
        linguists_table=linguists_table,
        tasktypes_table=tasktypes_table,
    )
