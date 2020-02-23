from application import db
from application import login_manager
from flask_login import UserMixin
from datetime import datetime

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(1000), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
        'User ID: ', self.user_id, '\r\n',
        'Title: ', self.title, '\r\n', self.content
            ])

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    reviews = db.relationship('Reviews', backref='author', lazy=True)

def __repr__(self):
    return ''.join([
        'User ID: ', str(self.id), '\r\n',
        'Email: ', self.email, '\r\n',
        'Name: ', self.first_name, ' ', self.last_name
    ])

#store

class Products(db.Model, UserMixin):
    productcode = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(30), nullable=False)
    productvendor = db.Column(db.String(30), nullable=False)
    productdescription= db.Column(db.String(150), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)


def __repr__(self):
    return ''.join([
        'Product Code: ', str(self.productcode), '\r\n',
        'Name: ', self.productname, '\r\n',
        'Vendor: ', self.productvendor, '\r\n',
        'Description: ', self.productdescription, '\r\n',
        'Price: ', self.price, '\r\n',
])

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))



#favourite

class Favou(db.Model):
    favou = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    productcode = db.Column(db.Integer, db.ForeignKey('products.productcode'), nullable=False)

def __repr__(self):
    return''.join([
       'Favourite:',str(self.id), '\r\n',
       'Id user:',self.id, '\r\n',
       'Product Name',self.productname,'\r\n',
])
