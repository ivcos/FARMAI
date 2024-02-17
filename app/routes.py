
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
from app.forms import ContactUSForm
from app.forms import farmtankStorageForm, farmtankCalculationForm
import shelve
import csv
import datetime
import pickle


@app.route('/login', methods=['GET', 'POST'])
# View function mapped to /login URL that creates an instance of the LoginForm
def login():
   #instantiate the form class
   form = LoginForm()
   # print(form.username.data)
   # print(form.password.data)
   # Check if user is registered and fields entered are valid
   shelve_file = shelve.open("users.db")
   # print(type(shelve_file))
   if request.method == 'POST':
      if form.username.data in shelve_file.keys():
         # print("User is registered")
         flash('User {} is registered'.format(form.username.data))
      else:
         # print("User is not registered")
         flash('User {} is not registered'.format(form.username.data)) 
         return redirect(url_for('.register')) 
      if form.password.data == shelve_file[form.username.data][1]:
         # print("Password is correct")
         flash('Password is correct')
         return redirect(url_for('.farmtankstorage'))
      else:
         # print("Password is incorrect")
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
      print("Items in the sample shelve file: ", (shelvefiledict.items()))
      emailsregistered = [email[0] for email in shelvefiledict.values()]
      print("Emails Registered", emailsregistered)
      shelvefile.close()
      form = RegistrationForm()
      if form.validate_on_submit():
         userRegistration = User(form.username.data, form.email.data, form.password.data)
         if form.username.data in shelvefiledict.keys():
            print("User already registered")
            error = "User " + form.username.data + " already registered. Please Use different Username"
            flash('User {} is already registered'.format(form.username.data))
            return render_template('register.html', title='Register', form = form, error=error)
         elif form.email.data in emailsregistered:
            print(shelvefiledict.values())
            print("Email already registered")
            error = "Email " + form.email.data + " already registered. Please Use different Email"
            flash('Email {} is already registered'.format(form.email.data))
            return render_template('register.html', title='Register', form = form, error=error)
         else:
            print(form.email.data)
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
            msg="Thank you. User " + form.username.data + " has been registered"
            print(msg)
            return redirect(url_for('.login', msg=msg))
      return render_template('register.html', title='Register', form=form)


@app.route('/farmtankstorage', methods=['GET', 'POST'])
def farmtankstorage():
      form = farmtankStorageForm()
      print("-----------------")
      print(form.farmnumber.data)
      print(form.tanklength.data)
      print("-----------------")
      if request.method == 'POST':
         print("Form Submitted")
         if form.validate_on_submit():
            print(form.farmnumber.data)
            print(form.tanklength.data)
            print("ok")
            #form=farmtankStorageForm(form.farmnumber.data, form.tanklength.data, form.tankwidth.data, form.tankheight.data, form.tankcapacity.data, form.regulatoryfillcapacityallowed.data, form.dateanimalshoused.data, form.tankheightdateanimalshoused.data, form.tankcapacityhousing.data) 
            # import the sensors data to check the height of the tank the date entered
            # on the form that the animals were housed.
            sensordatalist = loadcsvfile()
            #print(sensordatalist)
            sensordatalistlength = len(sensordatalist)
            for sensorreading in sensordatalist:
               # print(sensorreading[0])
               # print(form.dateanimalshoused.data)
               if sensorreading[0] == form.dateanimalshoused.data:
                  print("Date Animals Housed_0: ", form.dateanimalshoused.data)
                  print("Date Animals Housed: ", sensorreading[0])
                  print("test", form.dateanimalshoused.data)
                  print("Tank Height Date Animals Housed: ", sensorreading[2])
                  print("Day Number: ", sensorreading[1])
                  print(float(form.tanklength.data), float(form.tankwidth.data), float(form.tankheight.data))
                  tankcapacityfull = float(form.tanklength.data) * float(form.tankwidth.data) * float(form.tankheight.data)
                  availablecapacityatanimalhousing = float(form.tanklength.data) * float(form.tankwidth.data) * (float(form.tankheight.data)-(float(sensorreading[2]))/100)
                  print("Remaining Tank Capacity at date of Housing:", tankcapacityfull-availablecapacityatanimalhousing)
                  fillcapacpitatdateofhousing = tankcapacityfull-availablecapacityatanimalhousing
                  print("Remaining Tank Capacity at date of Housing:", fillcapacpitatdateofhousing)
                  print("Tank Fill Level at date of Housing:", tankcapacityfull-fillcapacpitatdateofhousing) 
                  print("percentagefill", 100 * (tankcapacityfull-fillcapacpitatdateofhousing)/tankcapacityfull)
                  print(tankcapacityfull)
                  print(type(tankcapacityfull))
                  # print("Remaining Tank Capacity at date of Housing:", 
                  #       (float(form.tanklength.data) * float(form.tankwidth.data) * (float(form.tankheight.data)-(float(sensorreading[2]))/100)))
                  # form.tankheightdateanimalshoused.data = sensorreading[1]
                  # print(100*tankcapacityhousing/tankcapacityfull)
                  form.tankheightdateanimalshoused.data = sensorreading[2]
                  form.tankcapacityhousing.data = fillcapacpitatdateofhousing
                  print(form.farmnumber.data)
                  header= ['Date', 'Tank Sensor Height Measurement(cm)', 'Available Tank Capacity(%)']
                  data = []
                  regressor_model = pickle.load(open('app/data/sensor-regessor-model.pk1','rb'))
                  print(int(sensorreading[1]))
                  print(type(sensorreading[1]))
                  zeroprecictedsensorheightreached = False
                  while not zeroprecictedsensorheightreached:
                     for sensorreading in sensordatalist:
                        #print(sensorreading)
                        sensorreading[1] = int(sensorreading[1])
                        #print(type(sensorreading[1]))
                        predictedvalue = regressor_model.predict([[sensorreading[1]]])
                        availablecapacity = 100 * (tankcapacityfull - (float(form.tanklength.data) * float(form.tankwidth.data) * (float(form.tankheight.data)-(float(predictedvalue))/100)))/tankcapacityfull
                        print("percentagefill", availablecapacity)
                        #data.append((sensorreading[0], sensorreading[1]), regressor_model.predict(sensorreading[[1]]))
                        #data.append([sensorreading[0], sensorreading[1], predictedvalue, availablecapacity])
                        data.append([sensorreading[0], int(round(predictedvalue[0], 0)), round(availablecapacity, 1)])
                        if predictedvalue < 1:
                           zeroprecictedsensorheightreached = True
                           break
                        #print(regressor_model.predict(sensorreading[[1]]))
                     # print("Tank Height Date Animals Housed: ", sensorreading[2])   	     
                     # return render_template('farmtankstorage.html', title='Slurry Storage', form=form)
                     return render_template('tankpredictions.html', title='Tank Predictions', data=data, header=header)
      else:
         return render_template('farmtankstorage.html', title='Slurry Storage', form=form)
      
@app.route('/ContactUs', methods=['GET', 'POST'])
def contactus():
   contactform = ContactUSForm()
   return render_template('ContactUs.html', title='ContactUs', form = contactform)



def loadcsvfile():  
   sensordatalist = []
   with open('app/data/sensors.csv', 'r') as file:
      reader = csv.reader(file)
      for row in reader:
         # change the time format from dd/mm/yyyy to yyyy-mm-dd
         # print(row[0])
         dateconverted= row[0]
         dateconverted = dateconverted[6:] + "-" + dateconverted[3:5] + "-" + dateconverted[:2]
         row[0] = dateconverted
         sensordatalist.append(row)
         # print(row)
   return sensordatalist

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