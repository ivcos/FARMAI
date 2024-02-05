from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
  password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=25)])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired() , Length(min=4, max=25)])
  email = StringField('Email', validators=[DataRequired(), Length(min=4, max=25)])
  password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=25)])
  password2 = PasswordField(
      'Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

    # def validate_username(self, username):
    #   user = User.query.filter_by(username=username.data).first()
    #   if user is not None:
    #     raise ValidationError('Please use a different username.')

    # def validate_email(self, email):
    #   user = User.query.filter_by(email=email.data).first()
    #   if user is not None:
    #     raise ValidationError('Please use a different email address.')


