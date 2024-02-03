
# The routes module handles the different URLS that the application implements.
# In Flask, hanlders for the application routes are called view functions.
# Views are mapped to one or more URLs so Flask knows what logic to execute
# when a client calls a given URL.
from app import app
from flask import render_template
from flask import request, redirect, url_for, flash
from app.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
# View function mapped to /login URL that creates an instance of the LoginForm
def login():
   #instantiate the form class
   form = LoginForm()
   print(form.username.data)
   print(form.password.data)
   if form.validate_on_submit():
      flash('Login requested for user {}, remember_me={}'.format(
         form.username.data, form.remember_me.data))
      return redirect(url_for('index'))
   return render_template('login.html', title='Sign In', form=form)


@app.route('/index')
def index():
    return render_template('index.html', title='Home')

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