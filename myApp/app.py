from flask import Flask,jsonify
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
from random import shuffle
from forms import *

loggedin=False
ad_loggedin=False
app = Flask(__name__)


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'	
app.config['MYSQL_PASSWORD']='#Neel1998'
app.config['MYSQL_DB']='NEWS'
app.config['MYSQL_CURSORCLASS']='DictCursor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:#Neel1998@localhost/NEWS'
db = SQLAlchemy(app)
mysql=MySQL(app)


un=""
pref=[]
complete=[]
total=[]

@app.route('/')
def index():
	setGeneral = set()
	listGeneral = []
	instGeneral = """select * from General order by date DESC"""
	tempcur=mysql.connection.cursor()
	tempcur.execute(instGeneral)
	general = tempcur.fetchall()
	tempcur.close()
	x=0
	for title in general:
		if title['title'] in setGeneral:
			pass 
		else:
			setGeneral.add(title['title'])
			if x<6:
				listGeneral.append(title)
				x+=1
	return render_template('home.html',homenews=listGeneral)

@app.route('/credits')
def credits():
	return render_template('about.html')

@app.route('/register',methods=['GET','POST'])
def register():
	form = RegisterForm(request.form)
	if request.method=='POST' and form.validate():
		name=request.form['name']
		email=request.form['email']
		usern=request.form['username']
		order =[]
		orderlist = ['Sports','Entertainment','General','Business','Health','Science','Technology']
		for category in orderlist:
			if request.form.get(category):
		 		order.append(category)
		
		order = ','.join(order)
		password=sha256_crypt.encrypt(str(request.form['password']))
		check=user.query.filter_by(username=usern).first()
		if(check is not None):
			flash("USERNAME ALREADY TAKEN")
			return render_template('register.html',form=form)
		else:
			newuser=user(name,usern,email,password,order)
			db.session.add(newuser)
			db.session.commit()
			return redirect(url_for('login'))
	return render_template('register.html',form=form)

@app.route('/register_admin',methods=['GET','POST'])
def register_admin():
	form = AdminForm(request.form)
	if request.method=='POST' and form.validate():
		name=request.form['name']
		email=request.form['email']
		usern=request.form['username']
		order =[]
		orderlist = ['Sports','Entertainment','General','Business','Health','Science','Technology']
		for category in orderlist:
			if request.form.get(category):
				order.append(category)
		
		order = ','.join(order)
		password=sha256_crypt.encrypt(str(request.form['password']))
		check=admin.query.filter_by(username=usern).first()
		if(check is not None):
			flash("USERNAME ALREADY TAKEN")
			return render_template('admin_register.html',form=form)
		else:
			newadmin=admin(name,usern,email,password,order)
			db.session.add(newadmin)
			db.session.commit()
			return redirect(url_for('login_admin'))
	return render_template('admin_register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
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
					global loggedin
					loggedin=True
					return redirect(url_for('user_home'))
				else:
					flash("AUTHENTICATION FAILED")
					return render_template('login.html')	
		else:
			flash("AUTHENTICATION FAILED")
			return render_template('login.html')
	return render_template('login.html')

@app.route('/login_admin',methods=['GET','POST'])
def login_admin():
	global ad_loggedin
	ad_loggedin=False
	if request.method=='POST':
		usern1=request.form['username']
		password_candidate=request.form['password']
		cur=mysql.connection.cursor()
		result=cur.execute("SELECT * FROM Admin WHERE username=%s",[usern1])
		if result >0:
				data=cur.fetchone()
				password=data['password']
				if sha256_crypt.verify(password_candidate,password):
					global un
					un=usern1
					global ad_loggedin
					ad_loggedin=True
					return redirect(url_for('admin_home'))
				else:
					flash("AUTHENTICATION FAILED")
					return render_template('login_admin.html')	
		else:
			flash("AUTHENTICATION FAILED")
			return render_template('login_admin.html')
	return render_template('login_admin.html')

@app.route('/logout')
def logout():
	session.clear()
	global loggedin
	loggedin=False
	global ad_loggedin
	ad_loggedin = False
	flash("Successfully logged out")
	return redirect(url_for('index'))

@app.route('/user_home',methods=['GET','POST'])
def user_home():
	cur=mysql.connection.cursor()
	us=cur.execute("SELECT * FROM userInfo WHERE username=%s",[un])
	order=cur.fetchone()['order']
	cur.close()
	cur=mysql.connection.cursor()
	order = order.split(',')
	setNews = set()
	listNews=[]
	if 'Sports' in order:
		cur.execute("""SELECT * FROM Sports """)
		news = cur.fetchall()
		count=0
		for title in news:
			if title['title'] in setNews:
				pass
			else:
				setNews.add(title['title'])
				listNews.append(title)

	if 'Entertainment' in order:
		cur.execute("""SELECT * FROM Entertainment """)
		news = cur.fetchall()
		count=0
		for title in news:
			if title['title'] in setNews:
				pass
			else:
				setNews.add(title['title'])
				listNews.append(title)
				
	if 'Health' in order:
		cur.execute("""SELECT * FROM Health """)
		news = cur.fetchall()
		count=0
		for title in news:
			if title['title'] in setNews:
				pass
			
			else:
				setNews.add(title['title'])
				listNews.append(title)
				
	if 'Business' in order:
		cur.execute("""SELECT * FROM Business """)
		news = cur.fetchall()
		
		for title in news:
			if title['title'] in setNews:
				pass
			else:
				setNews.add(title['title'])
				listNews.append(title)
				
	if 'General' in order:
		cur.execute("""SELECT * FROM General """)
		news = cur.fetchall()
		count=0
		for title in news:
			if title['title'] in setNews:
				pass
			
			else:
				setNews.add(title['title'])
				listNews.append(title)
				
	if 'Science' in order:
		cur.execute("""SELECT * FROM Science """)
		news = cur.fetchall()
		count=0
		for title in news:
			if title['title'] in setNews:
				pass
			
			else:
				setNews.add(title['title'])
				listNews.append(title)
				
	if 'Technology' in order:
		cur.execute("""SELECT * FROM Technology """)
		news = cur.fetchall()
		count=0
		for title in news:
			if title['title'] in setNews:
				pass
			else:
				setNews.add(title['title'])
				listNews.append(title)
	cur.close()
	shuffle(listNews)
	if request.method == 'POST':
		if 'Like' in request.form:
			title = request.form['title']
			userName = un
			cur=mysql.connection.cursor()
			temp=cur.execute("""SELECT * FROM Likes WHERE news= %s and user = %s""",[title,userName])
			if temp<=0:
				new = Likes(title,userName,1)
				db.session.add(new)
				db.session.commit()
			return redirect(url_for('user_home'))
	
			
		if 'Comments' in request.form:
			username = un
			title = request.form['title']
			comments = request.form['comment']
			new = Views(title,username,comments)
			db.session.add(new)
			db.session.commit()
			return redirect(url_for('user_home'))
	

		if ad_loggedin:
			if 'deleteComment' in request.form:
				uid=request.form['uid']
				cur=mysql.connection.cursor()
				cur.execute("""DELETE FROM Views where uid=%s""",[uid])
				mysql.connection.commit()
				cur.close() 
				return redirect(url_for('user_home'))
	
	

	cur=mysql.connection.cursor()
	temp=cur.execute("""SELECT news,count(likes) FROM Likes group by news""")
	likes = cur.fetchall()
	temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
	views = cur.fetchall()
	temp=cur.execute("""SELECT * FROM Likes where user = %s""",[un])
	liked = cur.fetchall()
	cur.close()
	if(loggedin):
		return render_template('logged.html',name=un,homenews=listNews,userloggedin=loggedin,likes=likes,views=views,liked=liked)
	else:
		return redirect(url_for('index'))
@app.route('/admin_home',methods = ['GET','POST'])
def admin_home():
	cur=mysql.connection.cursor()
	us=cur.execute("SELECT * FROM Admin WHERE username=%s",[un])
	order=cur.fetchone()['order']
	cur.close()
	cur=mysql.connection.cursor()
	order = order.split(',')
	setNews = set()
	listNews=[]
	if 'Sports' in order:
		p='Sports'
		command = """SELECT * FROM Sports"""
		cur.execute(command)
		news = cur.fetchall()
		count=0
		for title in news:
			if title['title'] in setNews:
				pass
			else:
				setNews.add(title['title'])
				listNews.append(title)

	if 'Entertainment' in order:
		cur.execute("""SELECT * FROM Entertainment """)
		news = cur.fetchall()
		count=0
		for title in news:
			if title['title'] in setNews:
				pass
			else:
				setNews.add(title['title'])
				listNews.append(title)
				
	if 'Health' in order:
		cur.execute("""SELECT * FROM Health """)
		news = cur.fetchall()
		count=0
		for title in news:
			if title['title'] in setNews:
				pass
			
			else:
				setNews.add(title['title'])
				listNews.append(title)
				
	if 'Business' in order:
		cur.execute("""SELECT * FROM Business """)
		news = cur.fetchall()
		
		for title in news:
			if title['title'] in setNews:
				pass
			else:
				setNews.add(title['title'])
				listNews.append(title)
				
	if 'General' in order:
		cur.execute("""SELECT * FROM General """)
		news = cur.fetchall()
		count=0
		for title in news:
			if title['title'] in setNews:
				pass
			
			else:
				setNews.add(title['title'])
				listNews.append(title)
				
	if 'Science' in order:
		cur.execute("""SELECT * FROM Science """)
		news = cur.fetchall()
		count=0
		for title in news:
			if title['title'] in setNews:
				pass
			
			else:
				setNews.add(title['title'])
				listNews.append(title)
				
	if 'Technology' in order:
		cur.execute("""SELECT * FROM Technology """)
		news = cur.fetchall()
		count=0
		for title in news:
			if title['title'] in setNews:
				pass
			else:
				setNews.add(title['title'])
				listNews.append(title)
	cur.close()
	shuffle(listNews)
	if request.method == 'POST':
		if 'Like' in request.form:
			title = request.form['title']
			userName = un
			cur=mysql.connection.cursor()
			temp=cur.execute("""SELECT * FROM Likes WHERE news= %s and user = %s""",[title,userName])
			if temp<=0:
				new = Likes(title,userName,1)
				db.session.add(new)
				db.session.commit()
			return redirect(url_for('admin_home'))
			
		if 'Comments' in request.form:
			username = un
			title = request.form['title']
			comments = request.form['comment']
			new = Views(title,username,comments)
			db.session.add(new)
			db.session.commit()
			return redirect(url_for('admin_home'))

		if ad_loggedin:
			if 'deleteComment' in request.form:
				uid=request.form['uid']
				cur=mysql.connection.cursor()
				cur.execute("""DELETE FROM Views where uid=%s""",[uid])
				mysql.connection.commit()
				cur.close() 
				return redirect(url_for('admin_home'))

	cur=mysql.connection.cursor()
	temp=cur.execute("""SELECT news,count(likes) FROM Likes group by news""")
	likes = cur.fetchall()
	temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
	views = cur.fetchall()
	temp=cur.execute("""SELECT * FROM Likes where user = %s""",[un])
	liked = cur.fetchall()
	cur.close()
	if(ad_loggedin):
		return render_template('logged.html',name=un,homenews=listNews,adminloggedin=ad_loggedin,likes=likes,views=views,liked=liked)
	else:
		return redirect(url_for('index'))

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

@app.route('/sports',methods=['GET','POST'])
def sportPage():
	setSports = set()
	listSports = []
	tempcur=mysql.connection.cursor()
	tempcur.execute("select * from Sports order by date DESC")
	sports = tempcur.fetchall()
	for title in sports:
		if title['title'] in setSports:
			pass 
		else:
			setSports.add(title['title'])
			listSports.append(title)
	cur=mysql.connection.cursor()
	temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
	views = cur.fetchall()
	cur.close()
	if loggedin==False and ad_loggedin == False:
		return render_template('news.html',khabar = listSports,views=views)
	
	else:
		if request.method == 'POST':
			if 'Like' in request.form:
				title = request.form['title']
				userName = un
				cur=mysql.connection.cursor()
				temp=cur.execute("""SELECT * FROM Likes WHERE news= %s and user = %s""",[title,userName])
				if temp<=0:
					new = Likes(title,userName,1)
					db.session.add(new)
					db.session.commit()
				return redirect(url_for('sportPage'))
			
			if 'Comments' in request.form:
				username = un
				title = request.form['title']
				comments = request.form['comment']
				new = Views(title,username,comments)
				db.session.add(new)
				db.session.commit()
				return redirect(url_for('sportPage'))

			if ad_loggedin:
				if 'deleteComment' in request.form:
					uid=request.form['uid']
					cur=mysql.connection.cursor()
					cur.execute("""DELETE FROM Views where uid=%s""",[uid])
					mysql.connection.commit()
					cur.close() 
					return redirect(url_for('sportPage'))



		cur=mysql.connection.cursor()
		temp=cur.execute("""SELECT news,count(likes) FROM Likes group by news""")
		likes = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
		views = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Likes where user = %s""",[un])
		liked = cur.fetchall()
		cur.close()
		print(ad_loggedin)
		return render_template('news_user.html',khabar = listSports,name=un,likes=likes,views=views,liked=liked,loggedin=loggedin,adminloggedin=ad_loggedin)
	


@app.route('/general',methods=['GET','POST'])
def generalPage():
	tempcur=mysql.connection.cursor()
	tempcur.execute("select * from General order by date DESC")
	setGeneral = set()
	listGeneral = []
	general = tempcur.fetchall()
	for title in general:
		if title['title'] in setGeneral:
			pass 
		else:
			setGeneral.add(title['title'])
			listGeneral.append(title)
	cur=mysql.connection.cursor()
	temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
	views = cur.fetchall()
	cur.close()
	if loggedin==False and ad_loggedin == False:
		return render_template('news.html',khabar = listGeneral,views=views)
	else:
		if request.method == 'POST':
			if 'Like' in request.form:
				title = request.form['title']
				userName = un
				cur=mysql.connection.cursor()
				temp=cur.execute("""SELECT * FROM Likes WHERE news= %s and user = %s""",[title,userName])
				if temp<=0:
					new = Likes(title,userName,1)
					db.session.add(new)
					db.session.commit()
				return redirect(url_for('generalPage'))
			
			if 'Comments' in request.form:
				username = un
				title = request.form['title']
				comments = request.form['comment']
				new = Views(title,username,comments)
				db.session.add(new)
				db.session.commit()
				return redirect(url_for('generalPage'))

			if ad_loggedin:
				if 'deleteComment' in request.form:
					uid=request.form['uid']
					cur=mysql.connection.cursor()
					cur.execute("""DELETE FROM Views where uid=%s""",[uid])
					mysql.connection.commit()
					cur.close() 
					return redirect(url_for('generalPage'))

		cur=mysql.connection.cursor()
		temp=cur.execute("""SELECT news,count(likes) FROM Likes group by news""")
		likes = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
		views = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Likes where user = %s""",[un])
		liked = cur.fetchall()
		cur.close()
		return render_template('news_user.html',khabar = listGeneral,name=un,likes=likes,views=views,liked=liked,loggedin=loggedin,adminloggedin=ad_loggedin)

@app.route('/entertainment',methods=['GET','POST'])
def entertainmentPage():
	setEntertainment = set()
	listEntertainment = []
	tempcur=mysql.connection.cursor()
	tempcur.execute("select * from Entertainment order by date DESC")
	entertainment = tempcur.fetchall()
	for title in entertainment:
		if title['title'] in setEntertainment:
			pass 
		else:
			setEntertainment.add(title['title'])
			listEntertainment.append(title)
	cur=mysql.connection.cursor()
	temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
	views = cur.fetchall()
	cur.close()
	if loggedin==False and ad_loggedin == False:
		return render_template('news.html',khabar= listEntertainment,views=views)
	else:
		if request.method == 'POST':
			if 'Like' in request.form:
				title = request.form['title']
				userName = un
				cur=mysql.connection.cursor()
				temp=cur.execute("""SELECT * FROM Likes WHERE news= %s and user = %s""",[title,userName])
				if temp<=0:
					new = Likes(title,userName,1)
					db.session.add(new)
					db.session.commit()
				return redirect(url_for('entertainmentPage'))
			if 'Comments' in request.form:
				username = un
				title = request.form['title']
				comments = request.form['comment']
				new = Views(title,username,comments)
				db.session.add(new)
				db.session.commit()
				return redirect(url_for('entertainmentPage'))

			if ad_loggedin:
				if 'deleteComment' in request.form:
					uid=request.form['uid']
					cur=mysql.connection.cursor()
					cur.execute("""DELETE FROM Views where uid=%s""",[uid])
					mysql.connection.commit()
					cur.close() 
					return redirect(url_for('entertainmentPage'))

		cur=mysql.connection.cursor()
		temp=cur.execute("""SELECT news,count(likes) FROM Likes group by news""")
		likes = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
		views = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Likes where user = %s""",[un])
		liked = cur.fetchall()
		cur.close()
		return render_template('news_user.html',khabar = listEntertainment,name=un,likes=likes,views=views,liked=liked,loggedin=loggedin,adminloggedin=ad_loggedin)

@app.route('/technology',methods=['GET','POST'])
def technologyPage():
	setTechnology = set()
	listTechnology = []
	tempcur=mysql.connection.cursor()
	tempcur.execute("select * from Technology order by date DESC")
	technology = tempcur.fetchall()
	for title in technology:
		if title['title'] in setTechnology:
			pass 
		else:
			setTechnology.add(title['title'])
			listTechnology.append(title)
	cur=mysql.connection.cursor()
	temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
	views = cur.fetchall()
	cur.close()
	if loggedin==False and ad_loggedin==False:
		return render_template('news.html',khabar = listTechnology,views=views)
	else:
		if request.method == 'POST':
			if 'Like' in request.form:
				title = request.form['title']
				userName = un
				cur=mysql.connection.cursor()
				temp=cur.execute("""SELECT * FROM Likes WHERE news= %s and user = %s""",[title,userName])
				if temp<=0:
					new = Likes(title,userName,1)
					db.session.add(new)
					db.session.commit()
				return redirect(url_for('technologyPage'))
			if 'Comments' in request.form:
				username = un
				title = request.form['title']
				comments = request.form['comment']
				new = Views(title,username,comments)
				db.session.add(new)
				db.session.commit()
				return redirect(url_for('technologyPage'))

			if ad_loggedin:
				if 'deleteComment' in request.form:
					uid=request.form['uid']
					cur=mysql.connection.cursor()
					cur.execute("""DELETE FROM Views where uid=%s""",[uid])
					mysql.connection.commit()
					cur.close() 
					return redirect(url_for('technologyPage'))

		cur=mysql.connection.cursor()
		temp=cur.execute("""SELECT news,count(likes) FROM Likes group by news""")
		likes = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
		views = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Likes where user = %s""",[un])
		liked = cur.fetchall()
		cur.close()
		return render_template('news_user.html',khabar = listTechnology,name=un,likes=likes,views=views,liked=liked,loggedin=loggedin,adminloggedin=ad_loggedin)

@app.route('/science',methods=['GET','POST'])
def sciencePage():
	setScience = set()
	listScience = []
	tempcur=mysql.connection.cursor()
	tempcur.execute("select * from Science order by date DESC")
	science = tempcur.fetchall()
	for title in science:
		if title['title'] in setScience:
			pass 
		else:
			setScience.add(title['title'])
			listScience.append(title)
	cur=mysql.connection.cursor()
	temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
	views = cur.fetchall()
	cur.close()
	if loggedin==False and ad_loggedin == False:
		return render_template('news.html',khabar = listScience,views=views)
	else:
		if request.method == 'POST':
			if 'Like' in request.form:
				title = request.form['title']
				userName = un
				cur=mysql.connection.cursor()
				temp=cur.execute("""SELECT * FROM Likes WHERE news= %s and user = %s""",[title,userName])
				if temp<=0:
					new = Likes(title,userName,1)
					db.session.add(new)
					db.session.commit()
				return redirect(url_for('sciencePage'))
			if 'Comments' in request.form:
				username = un
				title = request.form['title']
				comments = request.form['comment']
				new = Views(title,username,comments)
				db.session.add(new)
				db.session.commit()
				return redirect(url_for('sciencePage'))


			if ad_loggedin:
				if 'deleteComment' in request.form:
					uid=request.form['uid']
					cur=mysql.connection.cursor()
					cur.execute("""DELETE FROM Views where uid=%s""",[uid])
					mysql.connection.commit()
					cur.close() 
					return redirect(url_for('sciencePage'))

		cur=mysql.connection.cursor()
		temp=cur.execute("""SELECT news,count(likes) FROM Likes group by news""")
		likes = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
		views = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Likes where user = %s""",[un])
		liked = cur.fetchall()
		cur.close()
		return render_template('news_user.html',khabar = listScience,name=un,likes=likes,views=views,liked=liked,loggedin=loggedin,adminloggedin=ad_loggedin)

@app.route('/business',methods=['GET','POST'])
def businessPage():
	setBusiness = set()
	listBusiness = []
	tempcur=mysql.connection.cursor()
	tempcur.execute("select * from Business order by date DESC")
	business = tempcur.fetchall()
	for title in business:
		if title['title'] in setBusiness:
			pass 
		else:
			setBusiness.add(title['title'])
			listBusiness.append(title)
	cur=mysql.connection.cursor()
	temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
	views = cur.fetchall()
	cur.close()
	if loggedin==False and ad_loggedin==False:
		return render_template('news.html',khabar = listBusiness,views=views)
	else:
		if request.method == 'POST':
			if 'Like' in request.form:
				title = request.form['title']
				userName = un
				cur=mysql.connection.cursor()
				temp=cur.execute("""SELECT * FROM Likes WHERE news= %s and user = %s""",[title,userName])
				if temp<=0:
					new = Likes(title,userName,1)
					db.session.add(new)
					db.session.commit()
				return redirect(url_for('businessPage'))
			if 'Comments' in request.form:
				username = un
				title = request.form['title']
				comments = request.form['comment']
				new = Views(title,username,comments)
				db.session.add(new)
				db.session.commit()
				return redirect(url_for('businessPage'))


			if ad_loggedin:
				if 'deleteComment' in request.form:
					uid=request.form['uid']
					cur=mysql.connection.cursor()
					cur.execute("""DELETE FROM Views where uid=%s""",[uid])
					mysql.connection.commit()
					cur.close() 
					return redirect(url_for('businessPage'))

		cur=mysql.connection.cursor()
		temp=cur.execute("""SELECT news,count(likes) FROM Likes group by news""")
		likes = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
		views = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Likes where user = %s""",[un])
		liked = cur.fetchall()
		cur.close()
		return render_template('news_user.html',khabar = listBusiness,name=un,likes=likes,views=views,liked=liked,loggedin=loggedin,adminloggedin=ad_loggedin)

@app.route('/health',methods=['GET','POST'])
def healthPage():
	setHealth = set()
	listHealth = []
	tempcur=mysql.connection.cursor()
	tempcur.execute("select * from Health order by date DESC")
	health = tempcur.fetchall()
	for title in health:
		if title['title'] in setHealth:
			pass 
		else:
			setHealth.add(title['title'])
			listHealth.append(title)
	cur=mysql.connection.cursor()
	temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
	views = cur.fetchall()
	cur.close()
	if loggedin==False and ad_loggedin==False:
		return render_template('news.html',khabar = listHealth,views=views)
	else:
		if request.method == 'POST':
			if 'Like' in request.form:
				title = request.form['title']
				userName = un
				cur=mysql.connection.cursor()
				temp=cur.execute("""SELECT * FROM Likes WHERE news= %s and user = %s""",[title,userName])
				if temp<=0:
					new = Likes(title,userName,1)
					db.session.add(new)
					db.session.commit()
				return redirect(url_for('healthPage'))

			if 'Comments' in request.form:
				username = un
				title = request.form['title']
				comments = request.form['comment']
				new = Views(title,username,comments)
				db.session.add(new)
				db.session.commit()
				return redirect(url_for('healthPage'))

			if ad_loggedin:
				if 'deleteComment' in request.form:
					uid=request.form['uid']
					cur=mysql.connection.cursor()
					cur.execute("""DELETE FROM Views where uid=%s""",[uid])
					mysql.connection.commit()
					cur.close() 
					return redirect(url_for('healthPage'))

		cur=mysql.connection.cursor()
		temp=cur.execute("""SELECT news,count(likes) FROM Likes group by news""")
		likes = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
		views = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Likes where user = %s""",[un])
		liked = cur.fetchall()
		cur.close()
		return render_template('news_user.html',khabar = listHealth,name=un,likes=likes,views=views,liked=liked,loggedin=loggedin,adminloggedin=ad_loggedin)


@app.route('/add',methods=['GET','POST'])
def add():
	if request.method=='POST':
		title=request.form['title']
		author=request.form['author']
		category=request.form['category']
		summary=request.form['summary']
		description=request.form['description']
		date=request.form['date']
		k1=request.form['k1']
		k2=request.form['k2']
		k3=request.form['k3']
		url=request.form['url']
		urlimg=request.form['urlimg']
		if category.lower()=="sports":
			for i in k1,k2,k3:
				s=Sports(title,author,date,summary,url,description,urlimg,i)
				db.session.add(s)
				db.session.commit()
		elif category.lower()=="general":
			for i in k1,k2,k3:
				s=General(title,author,date,summary,url,description,urlimg,i)
				db.session.add(s)
				db.session.commit()
		elif category.lower()=="business":
			for i in k1,k2,k3:
				s=Business(title,author,date,summary,url,description,urlimg,i)
				db.session.add(s)
				db.session.commit()
		elif category.lower()=="health":
			for i in k1,k2,k3:
				s=Health(title,author,date,summary,url,description,urlimg,i)
				db.session.add(s)
				db.session.commit()
		elif category.lower()=="technology":
			for i in k1,k2,k3:
				s=Technology(title,author,date,summary,url,description,urlimg,i)
				db.session.add(s)
				db.session.commit()
		elif category.lower()=="science":
			for i in k1,k2,k3:
				s=Science(title,author,date,summary,url,description,urlimg,i)
				db.session.add(s)
				db.session.commit()
		elif category.lower()=="entertainment":
			for i in k1,k2,k3:
				s=Entertainment(title,author,date,summary,url,description,urlimg,i)
				db.session.add(s)
				db.session.commit()
		
		return render_template('addArticle.html')

	return render_template('addArticle.html')

@app.route('/delete',methods = ['GET','POST'])
def delete():
	pass

@app.route('/search',methods = ['GET','POST'])
def search():
	if request.method == 'POST':
		keyword = request.form.get('keyword',None)
		return redirect(url_for('result',keywords=keyword))
	if loggedin==False and ad_loggedin == False:
		return render_template('search.html')
	else:
		return render_template('search_user.html',name=un,loggedin=loggedin,adminloggedin=ad_loggedin)		

@app.route('/search/<keywords>',methods = ['GET','POST'])
def result(keywords):
	tables = ['General','Sports','Entertainment','Technology','Science']
	totalSet = set()
	total.clear()
	totalSet.clear()
	flag=0
	
	tempcur=mysql.connection.cursor()
	temp=tempcur.execute("select * from Sports where keyword=%s",[keywords])
	complete=tempcur.fetchall()
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
	
	
	temp=tempcur.execute("select * from General where keyword=%s",[keywords])
	complete=tempcur.fetchall()
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
	
	
	temp=tempcur.execute("select * from Entertainment where keyword=%s",[keywords])
	complete=tempcur.fetchall()
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

	
	temp=tempcur.execute("select * from Technology where keyword=%s",[keywords])
	complete=tempcur.fetchall()
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
	
	tempcur=mysql.connection.cursor()
	temp=tempcur.execute("select * from Science where keyword=%s",[keywords])
	complete=tempcur.fetchall()
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

	temp=tempcur.execute("select * from Business where keyword=%s",[keywords])
	complete=tempcur.fetchall()
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


	temp=tempcur.execute("select * from Health where keyword=%s",[keywords])
	complete=tempcur.fetchall()
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
	
	tempcur.close()
	cur=mysql.connection.cursor()
	temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
	views = cur.fetchall()
	cur.close()
	if loggedin==False and ad_loggedin==False:
		return render_template('results.html',results=total,keyword=keywords,views=views)
	else:
		if request.method == 'POST':
			if 'Like' in request.form:
				print("Liked clicked")
				title = request.form['title']
				userName = un
				cur=mysql.connection.cursor()
				temp=cur.execute("""SELECT * FROM Likes WHERE news= %s and user = %s""",[title,userName])
				if temp<=0:
					new = Likes(title,userName,1)
					db.session.add(new)
					db.session.commit()
				return redirect(url_for('result',keywords=keywords))
			
			if 'Comments' in request.form:
				username = un
				title = request.form['title']
				comments = request.form['comment']
				new = Views(title,username,comments)
				db.session.add(new)
				db.session.commit()
				return redirect(url_for('result',keywords=keywords))

			if ad_loggedin:
				if 'delete' in request.form:
					title=request.form['title']
					cur=mysql.connection.cursor()
					cur.execute("""DELETE FROM General where title=%s""",[title])
					cur.execute("""DELETE FROM Sports where title=%s""",[title])
					cur.execute("""DELETE FROM Health where title=%s""",[title])
					cur.execute("""DELETE FROM Business where title=%s""",[title])
					cur.execute("""DELETE FROM Science where title=%s""",[title])
					cur.execute("""DELETE FROM Technology where title=%s""",[title])
					cur.execute("""DELETE FROM Entertainment where title=%s""",[title])
					cur.execute("""DELETE FROM Views where news=%s""",[title])
					cur.execute("""DELETE FROM Likes where news=%s""",[title])
					mysql.connection.commit()
					cur.close() 
					return redirect(url_for('result',keywords=keywords))

				if 'deleteComment' in request.form:
					uid=request.form['uid']
					cur=mysql.connection.cursor()
					cur.execute("""DELETE FROM Views where uid=%s""",[uid])
					mysql.connection.commit()
					cur.close() 
					return redirect(url_for('result',keywords=keywords))


		cur=mysql.connection.cursor()
		temp=cur.execute("""SELECT news,count(likes) FROM Likes group by news""")
		likes = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Views ORDER BY uid DESC""")
		views = cur.fetchall()
		temp=cur.execute("""SELECT * FROM Likes where user = %s""",[un])
		liked = cur.fetchall()
		cur.close()
		return render_template('result_user.html',results = total,keyword =keywords,name=un,likes=likes,views=views,liked=liked,loggedin=loggedin,adminloggedin=ad_loggedin)
@app.errorhandler(404)
def err(e):
	return render_template('404.html')

if __name__=='__main__':
	app.secret_key=("secretkey")
	app.debug=True
	app.run()