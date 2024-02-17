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
    # self.__users[userRegistration.get_username()] = userRegistration.get_username()
    # self.__users[userRegistration.get_email()] = userRegistration.get_email()
    # self.__users[userRegistration.get_password()] = userRegistration.get_password()
    self.__users[userRegistration.get_username()] = [userRegistration.get_email(), userRegistration.get_password()]
    # self.users.sync()
  # Method to add a user to the shelve database
    
			
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
    
    