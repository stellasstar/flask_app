import datetime

from flask import Flask, session, request, flash, url_for, redirect, render_template, abort ,g
import flask.ext.login as flask_login
from flask.ext.login import LoginManager
from flask.ext.login import login_user , logout_user , current_user , login_required
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy

from models import User, app, db

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'] , 
                request.form['first_name'] ,
                request.form['last_name'] ,
                request.form['password'],
                request.form['email'],
                request.form['birthday'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('index.html', user=user)

@app.route('/logout')
def logout():
    flask_login.logout_user()
    flash('Logged out')
    return redirect(url_for('index'))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def dbinit(): 
     db.drop_all()
     db.create_all()
     print 'created db'
     db.session.add(User(username='eko', first_name='Eko',
                         last_name='Suprapto Wibowo', password='password',
                         email='swdev.bali@gmail.com',
                         birthday=datetime.date(1985, 1, 17)))

if __name__ == '__main__':
    dbinit()
    app.debug = True
    app.run()
