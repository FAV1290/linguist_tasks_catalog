from flask_wtf import FlaskForm
from wtforms import Field, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class LoginForm(FlaskForm):
    email = StringField('E-mail:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Sign in', description='invisible')
    action = '.process_login'

    def validate_email(form, field: Field) -> None:
        if not field.data.count('@'):
            raise ValidationError('Incorrect e-mail')

    @property
    def list_visible_fields(self) -> list[Field]:
        return [self.email, self.password]
