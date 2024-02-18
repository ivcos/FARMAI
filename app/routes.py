
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
   # shelve_file = shelve.open("users.db")
   shelve_file = shelve.open("app/data/users.db")
   if request.method == 'POST':
      if form.username.data in shelve_file.keys():
         flash('User {} logged in successfully'.format(form.username.data))
      else:
         flash('User {} is not registered'.format(form.username.data)) 
         return redirect(url_for('.register')) 
      if form.password.data == shelve_file[form.username.data][1]:
         # flash('Password is correct')
         return redirect(url_for('.farmtankstorage'))
      else:
         flash('Password is incorrect')
         return redirect(url_for('.login'))
   if form.validate_on_submit():
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
      shelvefile = shelve.open("app/data/users.db") 
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
            # flash('User {} is already registered'.format(form.username.data))
            return render_template('register.html', title='Register', form = form, error=error)
         elif form.email.data in emailsregistered:
            print(shelvefiledict.values())
            print("Email already registered")
            error = "Email " + form.email.data + " already registered. Please Use different Email"
            # flash('Email {} is already registered'.format(form.email.data))
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
      if request.method == 'POST':
         print("Form Submitted")
         if form.validate_on_submit():
            sensordatalist = loadcsvfile()
            sensordatalistlength = len(sensordatalist)
            for sensorreading in sensordatalist:
               if sensorreading[0] == form.dateanimalshoused.data:
                  tankcapacityfull = float(form.tanklength.data) * float(form.tankwidth.data) * float(form.tankheight.data)
                  availablecapacityatanimalhousing = float(form.tanklength.data) * float(form.tankwidth.data) * (float(form.tankheight.data)-(float(sensorreading[2]))/100)
                  print("Remaining Tank Capacity at date of Housing:", tankcapacityfull-availablecapacityatanimalhousing)
                  fillcapacpitatdateofhousing = tankcapacityfull-availablecapacityatanimalhousing
                  form.tankheightdateanimalshoused.data = sensorreading[2]
                  form.tankcapacityhousing.data = fillcapacpitatdateofhousing
                  print(form.farmnumber.data)
                  header= ['Date', 'Tank Sensor Height Measurement(cm)', 'Available Tank Capacity(%)']
                  data = []
                  regressor_model = pickle.load(open('app/data/sensor-regessor-model.pk1','rb'))
                  zeroprecictedsensorheightreached = False
                  while not zeroprecictedsensorheightreached:
                     for sensorreading in sensordatalist:
                        #print(sensorreading)
                        sensorreading[1] = int(sensorreading[1])
                        #print(type(sensorreading[1]))
                        predictedvalue = regressor_model.predict([[sensorreading[1]]])
                        availablecapacity = 100 * (tankcapacityfull - (float(form.tanklength.data) * float(form.tankwidth.data) * (float(form.tankheight.data)-(float(predictedvalue))/100)))/tankcapacityfull
                        print("percentagefill", availablecapacity)
                        data.append([sensorreading[0], int(round(predictedvalue[0], 0)), round(availablecapacity, 1)])
                        if predictedvalue < 1:
                           zeroprecictedsensorheightreached = True
                           break
                        
                     return render_template('tankpredictions.html', title='Tank Predictions', data=data, header=header)
      else:
         return render_template('farmtankstorage.html', title='Slurry Storage', form=form)
      
# @app.route('/ContactUs', methods=['GET', 'POST'])
# def contactus():
#    contactform = ContactUSForm()
#    return render_template('ContactUs.html', title='ContactUs', form = contactform)



def loadcsvfile():  
   sensordatalist = []
   with open('app/data/sensors.csv', 'r') as file:
      reader = csv.reader(file)
      for row in reader:
         # change the time format from dd/mm/yyyy to yyyy-mm-dd
         dateconverted= row[0]
         dateconverted = dateconverted[6:] + "-" + dateconverted[3:5] + "-" + dateconverted[:2]
         row[0] = dateconverted
         sensordatalist.append(row)
         # print(row)
   return sensordatalist

