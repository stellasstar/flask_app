import os
import unittest
import tempfile
from flask_sqlalchemy import SQLAlchemy

import urllib2
from flask import Flask
from flask_testing import LiveServerTestCase

db = SQLAlchemy()

def create_app(configfile):
    app = Flask(__name__)

    app.config.from_pyfile(config, silent=True)
    app.config['TESTING'] = True
    # Default port is 5000
    app.config['LIVESERVER_PORT'] = 8943
    db.init_app(app)

    # create routes, etc.

    return app

class MyappTestCase(unittest.TestCase):

    def setUp(self):
        # init test database, etc.
        app = create_app('config.py')
        self.app = app.test_client()

    def tearDown(self):
        app.close()
        db.session.remove()
        db.drop_all()

    def test_empty_db(self):
        app.run()
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data


class TestConnect(unittest.TestCase):

    def setUp(self):
        app = create_app('config.py')
        self.app = app.test_client()
        db.session.close()
        db.drop_all()
        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()


class MyTest(LiveServerTestCase):

    def setUp(self):
        app = create_app('config.py')
        self.app = app.test_client()

    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

if __name__ == '__main__':
    unittest.main()
