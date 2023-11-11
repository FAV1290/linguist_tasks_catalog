import uuid
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError
from wtforms import DateTimeField, Field, SelectField, StringField, PasswordField, SubmitField


from db.models import Client, TaskType, Linguist, Task
from webapp.form_choices_fillers import create_status_choices, create_name_to_id_choices


class LoginForm(FlaskForm):
    email = StringField('E-mail:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Sign in')

    def validate_email(form, field: Field) -> None:
        if not field.data.count('@'):
            raise ValidationError('Incorrect e-mail')

    @property
    def list_visible_fields(self) -> list[Field]:
        return [self.email, self.password]


class AddTaskForm(FlaskForm):
    name = StringField('Title:', validators=[DataRequired()])
    status = SelectField('Status:', validators=[DataRequired()])
    deadline_at = DateTimeField('Deadline:', format='%d/%m/%Y %H:%M', id='datetimepicker')
    runtime = StringField('Runtime:', validators=[DataRequired()])
    events = StringField('Events:', validators=[DataRequired()])
    client_id = SelectField('Client:', validators=[DataRequired()])
    type_id = SelectField('Task type:', validators=[DataRequired()])
    linguist_id = SelectField('Linguist:', validators=[DataRequired()])
    submit = SubmitField('Add task')

    @property
    def list_visible_fields(self) -> list[Field]:
        visible_fields = [
            self.name, self.status, self.deadline_at,
            self.runtime, self.events, self.client_id,
            self.type_id, self.linguist_id,
        ]
        return visible_fields

    def define_choices(self, profile_id: uuid.UUID) -> None:
        self.status.choices = create_status_choices()
        self.client_id.choices = create_name_to_id_choices(
            Client.fetch_user_clients, profile_id)
        self.type_id.choices = create_name_to_id_choices(
            TaskType.fetch_user_tasktypes, profile_id)
        self.linguist_id.choices = create_name_to_id_choices(
            Linguist.fetch_user_linguists, profile_id)

    def fill_with_task_data(self, task: Task) -> None:
        self.name.data = task.name
        self.status.data = task.status
        self.deadline_at.data = task.deadline_at
        self.runtime.data = task.runtime
        self.events.data = task.events
        self.client_id.data = task.client_id
        self.type_id.data = task.type_id
        self.linguist_id.data = task.linguist_id
        self.submit.label.text = 'Edit task'
