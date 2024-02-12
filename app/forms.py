from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import DecimalField, RadioField, SelectField, TextAreaField 
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

class farmtankStorageForm(FlaskForm):
  farmnumber = StringField('Farm Number', validators=[DataRequired(), Length(min=4, max=10)])
  tanklength = StringField('Tank Length', validators=[DataRequired()])
  tankwidth = StringField('Tank Width', validators=[DataRequired()])
  tankheight = StringField('Tank Height', validators=[DataRequired()])
  tankcapacity = StringField('Tank Fill Capacity')
  regulatoryfillcapacityallowed = StringField('Regulatory Fill Level Allowed')
  dateanimalshoused = StringField('Date Animals Housed', validators=[DataRequired()])
  tankheightdateanimalshoused = StringField('Tank Height Date Animals Housed')
  tankcapacityhousing = StringField('Tank Fill Capacity at date of Housing')
  # dateninetypercentfilled = StringField('Date Eighty Percent Filled')
  # datefull = StringField('Date Full')
        
  submit = SubmitField('Submit')
  submit2 = SubmitField('Reset')

class farmtankCalculationForm(FlaskForm):
  farmnumber = StringField('Farm Number', validators=[DataRequired(), Length(min=4, max=10)])
  # regulatoryfillLevelallowed = StringField('Regulatory Fill Level Allowed')
  #dateeightypercentfilled = StringField('Date Eighty Percent Filled')
  #dateninetypercentfilled = StringField('Date Eighty Percent Filled')
  datefull = StringField('Date Full')
  submit2 = SubmitField('Reset')

class ContactUSForm(FlaskForm):
  firstname = StringField('First Name', validators=[DataRequired()])
  lastname = StringField('Last Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Length(min=4, max=25)])
  mobilenumber = StringField('Mobile')
  farmtype = SelectField('Farm Type', validators=[DataRequired()], choices=[('Pig', 'Pig'), ('Poultry', 'Poultry'), ('Dairy', 'Dairy'), ('Beef', 'Beef'), ('Sheep', 'Sheep'), ('Other', 'Other')])  
  submit = SubmitField('Submit')
  
                         