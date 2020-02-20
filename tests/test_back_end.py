import unittest

from flask import abort, url_for
from flask_testing import TestCase
import os
from application import app, db
from application.models import Users, Posts
class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(
           SQLALCHEMY_DATABASE_URI=os.getevn("DB_URI"))
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password="admin2020")

        # create test non-admin user
        employee = Users(first_name="test", last_name="test", email="test@test.com", password="test2020")

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()
