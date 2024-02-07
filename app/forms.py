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

class SlurryStorageForm(FlaskForm):
  farmnumber = StringField('Farm Number', validators=[DataRequired(), Length(min=4, max=10)])
  tanklength = StringField('Tank Length', validators=[DataRequired()])
  tankwidth = StringField('Tank Width', validators=[DataRequired()])
  tankheight = StringField('Tank Height', validators=[DataRequired()])
  tankvolume = StringField('Tank Volume')
  tankcapacity = StringField('Tank Fill Capacity')
  date = StringField('Date', validators=[DataRequired()])
        
  submit = SubmitField('Submit')
  submit2 = SubmitField('Reset')

class SlurryCalculationForm(FlaskForm):
  farmnumber = StringField('Farm Number', validators=[DataRequired(), Length(min=4, max=10)])
  regulatoryfillLevelallowed = StringField('Regulatory Fill Level Allowed')
  dateeightypercentfilled = StringField('Date Eighty Percent Filled')
  dateninetypercentfilled = StringField('Date Eighty Percent Filled')
  datefull = StringField('Date Full')
  submit2 = SubmitField('Reset')


