from flask import Flask
from flask import flash
from flask import redirect
from flask import url_for
from flask import session
from flask import logging
from flask import render_template
from flask import request
from data import Articles
from flask_mysqldb import MySQL
import MySQLdb
import MySQLdb.cursors 
from wtforms import Form,StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from models import *
from models import db as pdb
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

#mysql = MySQLdb.connect(host = "localhost",user = "root",passwd = "#Neel1998",db="myapp",cursorclass=MySQLdb.cursors.DictCursor)
news = MySQLdb.connect(host = "localhost",user = "root",passwd = "aarush123@",db="NEWS")
newsCursor = news.cursor(cursorclass=MySQLdb.cursors.DictCursor)
un=""
pref=[]

@app.route('/')
def index():
	return render_template('home.html')
@app.route('/about')
def about():
	return render_template('about.html')
class RegisterForm(Form):
	name=StringField('Name',[validators.Length(min=1,max=50)])
	username=StringField('Username',[validators.Length(min=4,max=50)])
	email=StringField('Email',[validators.Length(min=4,max=50)])
	password=PasswordField('Password',[
		validators.DataRequired(),
		validators.EqualTo('confirm',message='Passwords do not match')
		])
	confirm=PasswordField('Confirm Password')
@app.route('/register',methods=['GET','POST'])
def register():
	form = RegisterForm(request.form)
	if request.method=='POST' and form.validate():
		name=request.form['name']
		email=request.form['email']
		usern=request.form['username']
		password=sha256_crypt.encrypt(str(request.form['password']))
		check=user.query.filter_by(username=usern).first()
		if(check is not None):
			flash("USERNAME ALREADY TAKEN")
			return render_template('register.html',form=form)
		else:
			newuser=user(name,usern,email,password)
			db.session.add(newuser)
			db.session.commit()
			return render_template('user_home.html',name=usern)
	return render_template('register.html',form=form)
@app.route('/login',methods=['GET','POST'])
def login():
	db.session.commit()
	if request.method=='POST':
		usern1=request.form['username']
		password_candidate=request.form['password']
		cur=mysql.connection.cursor()
		result=cur.execute("SELECT * FROM userInfo WHERE username=%s",[usern1])
		if result >0:
				data=cur.fetchone()
				password=data['password']
				if sha256_crypt.verify(password_candidate,password):
					global un
					un=usern1
					return render_template('user_home.html',name=usern1)
				else:
					flash("AUTHENTICATION FAILED")
					return render_template('login.html')	
		else:
			flash("AUTHENTICATION FAILED")
			return render_template('login.html')
	return render_template('login.html')
@app.route('/logout')
def logout():
	session.clear()
	return render_template('logout.html')
@app.route('/user_home')
def user_home():
	return render_template('user_home.html',name=un)
@app.route('/change',methods=['GET','POST'])
def change():
	if request.method=='POST':
		old_p=request.form['old_password']
		new_p=sha256_crypt.encrypt(str(request.form['new_password']))
		cur=mysql.connection.cursor()
		us=cur.execute("SELECT * FROM userInfo WHERE username=%s",[un])
		pas=cur.fetchone()['password']
		if sha256_crypt.verify(old_p,pas):
			cur.execute("UPDATE userInfo SET password=%s WHERE username=%s",[new_p,un])
			mysql.connection.commit()
			cur.close()
			return render_template('user_home.html',name=un)
		else:
			flash("OLD PASSWORD DOENT MATCH!!")
			return render_template('change.html',name=un)
	return render_template('change.html',name=un)
@app.route('/change_user',methods=['GET','POST'])
def change_user():
	if request.method=='POST':
		p=request.form['password']
		ns=request.form['new_user']
		cur=mysql.connection.cursor()
		result=cur.execute("SELECT * FROM userInfo WHERE username=%s",[un])
		data=cur.fetchone()
		password=data['password']
		if sha256_crypt.verify(p,password):
			cur.execute("UPDATE userInfo SET username=%s WHERE password=%s",[ns,password])
			global un
			un=ns
			mysql.connection.commit()
			cur.close()
			return render_template('user_home.html',name=un)
		else:
		   	flash("PASSWORD DOENT MATCH!!")
		   	return render_template('change_user.html',name=un)
	return render_template('change_user.html',name=un)
@app.route('/sports')
def sportPage():
	setSports = set()
	listSports = []
	instSports = """select * from Sports where date = '2018-04-08' """
	newsCursor.execute(instSports)
	sports = newsCursor.fetchall()
	for title in sports:
		if title['title'] in setSports:
			pass 
		else:
			setSports.add(title['title'])
			listSports.append(title)
	return render_template('sports.html',sports = listSports)
if __name__=='__main__':
	app.secret_key=("secretkey")
	app.debug=True
	app.run()
