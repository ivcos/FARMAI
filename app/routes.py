
# The routes module handles the different URLS that the application implements.
# In Flask, hanlders for the application routes are called view functions.
# Views are mapped to one or more URLs so Flask knows what logic to execute
# when a client calls a given URL.
from app import app
from flask import render_template
from flask import request, redirect, url_for, flash
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.models import User
from app.models import Usersdb
from app.forms import SlurryStorageForm, SlurryCalculationForm
import shelve


@app.route('/login', methods=['GET', 'POST'])
# View function mapped to /login URL that creates an instance of the LoginForm
def login():
   #instantiate the form class
   form = LoginForm()
   print(form.username.data)
   print(form.password.data)
   # Check if user is registered and fields are valid
   shelve_file = shelve.open("users.db")
   print(type(shelve_file))
   if request.method == 'POST':
      if form.username.data in shelve_file.keys():
         print("User is registered")
         flash('User {} is registered'.format(form.username.data))
      else:
         print("User is not registered")
         flash('User {} is not registered'.format(form.username.data)) 
         return redirect(url_for('.register')) 
      if form.password.data == shelve_file[form.username.data][1]:
         print("Password is correct")
         flash('Password is correct')
         return redirect(url_for('.index'))
      else:
         print("Password is incorrect")
         flash('Password is incorrect')
         return redirect(url_for('.login'))
   if form.validate_on_submit():
      #flash() function is a way to provide feedback to a user
      flash('Login requested for user {}, remember_me={}'.format(
         form.username.data, form.remember_me.data))
      return redirect(url_for('.index'))
   return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/logout')
def logout():
    return "<p>Logout</p>"

@app.route('/register',  methods=['GET', 'POST'])
def register():
      shelvefile = shelve.open("users.db") 
      shelvefiledict = dict(shelvefile)
      print("Items in the sample shelve file: ", list(shelvefiledict.items()))
      shelvefile.close()
      form = RegistrationForm()
      # print(form.username.data)
      # print(form.email.data)
      # print(form.password.data)
      # print(form.password2.data)
      if form.validate_on_submit():
         userRegistration = User(form.username.data, form.email.data, form.password.data)
         if form.username.data in shelvefiledict.keys():
            print("User already registered")
            error = "User " + form.username.data + " already registered. Please Use different Username"
            flash('User {} is already registered'.format(form.username.data))
            return render_template('register.html', title='Register', form = form, error=error)
         else:
            print("User not registered")
            flash('User {} is not registered'.format(form.username.data))
            print(userRegistration.username)
            print(userRegistration.email)
            print(userRegistration.password)
            userdb= Usersdb()
            userdb.add_user(userRegistration)
            userdb.__del__()
            flash('Registration requested for user {}, email={}'.format(
               form.username.data, form.email.data))
            # open a shelf file 
            #shelve_file = shelve.open("users.db") 
            print("Items in the sample shelve file: ", list(shelvefiledict.items())) 
            print() 
            return redirect(url_for('.login'))
      return render_template('register.html', title='Register', form=form)


@app.route('/slurryStorage', methods=['GET', 'POST'])
def slurrystorage():
      form = SlurryStorageForm()
      form2 = SlurryCalculationForm()
      return render_template('slurryStorage.html', title='Slurry Storage', form=form, form2=form2)
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'GET':
#        return render_template('login.html', title='Home') 
#     else:
#       username = request.form['username']
#       password = request.form['password']
#       if username != 'admin' or password != 'admin':
#          error = 'Invalid credentials. Please try again.'
#          print(username)
#          print(password)
#          return render_template('login.html', title='Home', error=error)       
#       else:
#         print(username)
#         print(password)
#         return redirect(url_for('home'))  

# the render_template function invokes the Jinia tempate. Jinja substitutes
#   {{ ... }} blocks with the corresponding values, given by the arguments