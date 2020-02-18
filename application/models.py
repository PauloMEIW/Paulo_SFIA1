from application import db
from application import login_manager
from flask_login import UserMixin
from datetime import datetime

class Posts(db.Model):
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
    posts = db.relationship('Posts', backref='author', lazy=True)
    products = db.relationship('Products', backref='first_name', lazy=True)

def __repr__(self):
    return ''.join([
        'User ID: ', str(self.id), '\r\n',
        'Email: ', self.email, '\r\n',
        'Name: ', self.first_name, ' ', self.last_name
    ])




#store

class Products(db.Model, UserMixin):
    productCode = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(30), nullable=False)
    productVendor = db.Column(db.String(30), nullable=False)
    productDescription= db.Column(db.String(150), nullable=False, unique=True)
    quantityInStock = db.Column(db.String(6), nullable=False)
    buyPrice = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

def __repr__(self):
    return ''.join([
        'Product Code: ', str(self.productCode), '\r\n',
        'Name: ', self.productName, '\r\n',
        'Vendor: ', self.productVendor, '\r\n',
        'Description: ', self.productDescription, '\r\n',
        'Quantity: ', self.quantityInStock, '\r\n',
        'Price: ', self.buyPrice, '\r\n',
])

#store
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

