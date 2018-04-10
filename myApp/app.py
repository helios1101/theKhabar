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
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:aarush123@@localhost/NEWS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
db = SQLAlchemy(app)
news = MySQLdb.connect(host = "localhost",user = "root",passwd = "aarush123@",db="NEWS")
newsCursor = news.cursor(cursorclass=MySQLdb.cursors.DictCursor)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='aarush123@'
app.config['MYSQL_DB']='NEWS'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql=MySQL(app)

un=""
pref=[]
complete=[]
total=[]

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
			#news.commit()
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
			#news.commit()
			return render_template('user_home.html',name=un)
		else:
		   	flash("PASSWORD DOENT MATCH!!")
		   	return render_template('change_user.html',name=un)
	return render_template('change_user.html',name=un)
@app.route('/sports')
def sportPage():
	setSports = set()
	listSports = []
	instSports = """select * from Sports order by date DESC"""
	newsCursor.execute(instSports)
	sports = newsCursor.fetchall()
	for title in sports:
		if title['title'] in setSports:
			pass 
		else:
			setSports.add(title['title'])
			listSports.append(title)
	return render_template('sports.html',sports = listSports)

@app.route('/general')
def generalPage():
	setGeneral = set()
	listGeneral = []
	instGeneral = """select * from General order by date DESC"""
	newsCursor.execute(instGeneral)
	general = newsCursor.fetchall()
	for title in general:
		if title['title'] in setGeneral:
			pass 
		else:
			setGeneral.add(title['title'])
			listGeneral.append(title)
	return render_template('general.html',general = listGeneral)

@app.route('/entertainment')
def entertainmentPage():
	setEntertainment = set()
	listEntertainment = []
	instEntertainment = """select * from Entertainment order by date DESC """
	newsCursor.execute(instEntertainment)
	entertainment = newsCursor.fetchall()
	for title in entertainment:
		if title['title'] in setEntertainment:
			pass 
		else:
			setEntertainment.add(title['title'])
			listEntertainment.append(title)
	return render_template('entertainment.html',entertainment = listEntertainment)

@app.route('/technology')
def technologyPage():
	setTechnology = set()
	listTechnology = []
	instTechnology = """select * from Technology order by date DESC """
	newsCursor.execute(instTechnology)
	technology = newsCursor.fetchall()
	for title in technology:
		if title['title'] in setTechnology:
			pass 
		else:
			setTechnology.add(title['title'])
			listTechnology.append(title)
	return render_template('technology.html',technology = listTechnology)

@app.route('/science')
def sciencePage():
	setScience = set()
	listScience = []
	instScience = """select * from Science """
	newsCursor.execute(instScience)
	science = newsCursor.fetchall()
	for title in science:
		if title['title'] in setScience:
			pass 
		else:
			setScience.add(title['title'])
			listScience.append(title)
	return render_template('science.html' , science = listScience)

@app.route('/business')
def businessPage():
	setBusiness = set()
	listBusiness = []
	instBusiness = """select * from Business """
	newsCursor.execute(instBusiness)
	business = newsCursor.fetchall()
	for title in business:
		if title['title'] in setBusiness:
			pass 
		else:
			setBusiness.add(title['title'])
			listBusiness.append(title)
	return render_template('business.html' , business = listBusiness)

@app.route('/health')
def healthPage():
	setHealth = set()
	listHealth = []
	instHealth = """select * from Health """
	newsCursor.execute(instHealth)
	health = newsCursor.fetchall()
	for title in health:
		if title['title'] in setHealth:
			pass 
		else:
			setHealth.add(title['title'])
			listHealth.append(title)
	return render_template('health.html' , health = listHealth)




@app.route('/search',methods = ['GET','POST'])
def search():
	if request.method == 'POST':
		keyword = request.form.get('keyword',None)
		return result(keyword)
			
	return render_template('search.html') 

@app.route('/search/<keywords>')
def result(keywords):
	tables = ['General','Sports','Entertainment','Technology','Science']
	totalSet = set()
	total.clear()
	totalSet.clear()
	flag=0
	temp=newsCursor.execute("""SELECT * FROM Sports WHERE keyword= %s """,[keywords])
	complete = newsCursor.fetchall()
	if temp <=0:
		pass
	else:	
		flag=1
		for khabar in complete:
			if khabar['title'] in totalSet:
				pass
		else:
			totalSet.add(khabar['title'])
			global total
			total.append(khabar)
	
	temp=newsCursor.execute("""SELECT * FROM General WHERE keyword= %s """,[keywords])
	complete = newsCursor.fetchall()
	if temp <=0:
		pass
	else:	
		flag=1
		for khabar in complete:
			if khabar['title'] in totalSet:
				pass
		else:
			totalSet.add(khabar['title'])
			global total
			total.append(khabar)
	
	temp=newsCursor.execute("""SELECT * FROM Entertainment WHERE keyword= %s """,[keywords])
	complete = newsCursor.fetchall()
	if temp <=0:
		pass
	else:	
		flag=1
		for khabar in complete:
			if khabar['title'] in totalSet:
				pass
		else:
			totalSet.add(khabar['title'])
			global total
			total.append(khabar)
	
	temp=newsCursor.execute("""SELECT * FROM Technology WHERE keyword= %s """,[keywords])
	complete = newsCursor.fetchall()
	if temp <=0:
		pass
	else:	
		flag=1
		for khabar in complete:
			if khabar['title'] in totalSet:
				pass
		else:
			totalSet.add(khabar['title'])
			global total
			total.append(khabar)
	
	temp=newsCursor.execute("""SELECT * FROM Science WHERE keyword= %s """,[keywords])
	complete = newsCursor.fetchall()
	if temp <=0:
		pass
	else:	
		flag=1
		for khabar in complete:
			if khabar['title'] in totalSet:
				pass
		else:
			totalSet.add(khabar['title'])
			global total
			total.append(khabar)

	temp=newsCursor.execute("""SELECT * FROM Business WHERE keyword= %s """,[keywords])
	complete = newsCursor.fetchall()
	if temp <=0:
		pass
	else:	
		flag=1
		for khabar in complete:
			if khabar['title'] in totalSet:
				pass
		else:
			totalSet.add(khabar['title'])
			global total
			total.append(khabar)

	temp=newsCursor.execute("""SELECT * FROM Health WHERE keyword= %s """,[keywords])
	complete = newsCursor.fetchall()
	if temp <=0:
		pass
	else:	
		flag=1
		for khabar in complete:
			if khabar['title'] in totalSet:
				pass
		else:
			totalSet.add(khabar['title'])
			global total
			total.append(khabar)
	
	if flag == 0:
		flash('Sorry,No results found :(')
		return redirect(url_for('search'))		
	return render_template('results.html',results = total,keyword =keywords)			

if __name__=='__main__':
	app.secret_key=("secretkey")
	app.debug=True
	app.run()
