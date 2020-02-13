from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] =str( os.getenv('MY_SECRET_KEY'))
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DB_URI'))
db = SQLAlchemy(app)

from application import routes
