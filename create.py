from application import db

db.drop_all()
db.create_all()

from application.models import Reviews
db.create_all()
