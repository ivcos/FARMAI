import shelve


class Usersdb:
  # Constructor for the Users_db class to store the users in a shelve database
  def __init__(self):
    self.__users = shelve.open('app/data/users.db')
    print(self.__users, "usersdb created")

  # destructor to close the shelve database
  def __del__(self):
    self.__users.close()

  def add_user(self, userRegistration):
    self.__users[userRegistration.get_username()] = [userRegistration.get_email(), userRegistration.get_password()]
    
  def add_contact(self, contactUser):
    self.__users[contactUser.get_email()] = [contactUser.get_firstname(), contactUser.get_lastname(), contactUser.get_mobilenumber()]
			
class User:

  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = password

  def __repr__(self):
    return '<User {}>'.format(self.username)
  
  def get_username(self):
    return self.username
  
  def get_email(self):
    return self.email
  
  def get_password(self): 
    return self.password
  

class SlurryStorageTank:

  def __init__(self, farmnumber, tanklength, tankwidth, tankheight):
    self.farmnumber = farmnumber
    self.tanklength = tanklength
    self.tankwidth = tankwidth
    self.tankheight = tankheight
    self.tankcapacity = self.tanklength * self.tankwidth * self.tankheight
    # self.regulatoryfillLevelallowed = self.tankcapacity * 0.8
    # self.eightypercentfilled = self.tankcapacity * 0.2
    # self.ninetypercentfilled = self.tankcapacity * 0.1
    # self.datefull = self.tankcapacity *0.8
    
class ContactUser:
  def __init__(self, firstname, lastname, email, mobilenumber):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.mobilenumber = mobilenumber

  def __repr__(self):
    return '<User {}>'.format(self.firstname)
      
  def get_firstname(self):
    return self.firstname
      
  def get_lastname(self):
    return self.lastname
      
  def get_email(self):
    return self.email
      
  def get_mobilenumber(self): 
    return self.mobilenumber

