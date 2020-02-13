from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy



from application import routes
<!-- esta linha de cima antes estava debaixo da db=SQLALchemy(app)............. -->

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



app = Flask(__name__)
app.config['SECRET_KEY'] =str( os.getenv('MY_SECRET_KEY'))
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DB_URI'))
db = SQLAlchemy(app)
