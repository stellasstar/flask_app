import datetime
import urllib2

from flask_testing import LiveServerTestCase
from flask import Flask, url_for
import unittest

from models import User, app, db


class appDBTests(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        self.client = app.test_client()
        self.ctx = app.app_context()
        self.app = app
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
        db.session.remove()
        db.drop_all()
        try:
            user = User.query.all()
        except Exception as e:
            assert e

    def test_setup(self):
        self.assertTrue(self.app is not None)
        self.assertTrue(self.client is not None)
        self.assertTrue(self.ctx is not None)

    def test_user_add(self):
        db.session.add(User(username='eko', first_name='Eko',
                         last_name='Suprapto Wibowo', password='password',
                         email='swdev.bali@gmail.com',
                         birthday=datetime.date(1985, 1, 17)))
        db.session.commit()
        user = User.query.filter_by(username='eko').first_or_404()
        assert user in db.session

# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()
