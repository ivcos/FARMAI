from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from flask_login import LoginManager
# Creates an application object as an instance of the class Flask
# imported from flask package
app = Flask(__name__)
# Tells the flas app to read and apply the configuration from the object
app.config.from_object(Config)
login=LoginManager(app)
from app import routes

#Allows you run the file from the command line
if __name__ == "__main__":
  app.run()