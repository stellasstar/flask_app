from flask import Flask
import unittest

from app import db
import models

class appDBTests(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        self.app = Flask(__name__)
        app.config['DEBUG'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        app.config.from_object('config.py')
        db = models.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.drop_all()



# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()
