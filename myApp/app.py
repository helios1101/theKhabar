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
from wtforms import Form,StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='#Neel1998'
app.config['MYSQL_DB']='myapp'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql=MySQL(app)

Articles=Articles();

un=""
pref=[]

@app.route('/')
def index():
	return render_template('home.html')
@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/articles')
def articles():
	return render_template('articles.html',articles=Articles)
@app.route('/article/<string:id>/')
def article(id):
	return render_template('article.html',id=id)
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
		name=form.name.data
		email=form.email.data
		username=form.username.data
		app.logger.info(form.sp.data)
		password=sha256_crypt.encrypt(str(form.password.data))
		cur=mysql.connection.cursor()
		cur.execute("SELECT * FROM users where username=%s",[username])
		if(cur.fetchone() is not None):
			flash("USERNAME ALREADY TAKEN")
			return render_template('register.html',form=form)
		else:
			cur.execute("INSERT INTO users(name,email,username,password) VALUES(%s,%s,%s,%s)",(name,email,username,password))
			mysql.connection.commit()
			cur.close()
			return render_template('home.html')

	return render_template('register.html',form=form)
@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='POST':
		username=request.form['username']
		password_candidate=request.form['password']
		cur=mysql.connection.cursor()
		result=cur.execute("SELECT * FROM users WHERE username=%s",[username])
		if result > 0 :
				data=cur.fetchone()
				password=data['password']
				if sha256_crypt.verify(password_candidate,password):
					global un
					un=username
					return render_template('user_home.html',name=username)
				else:
					flash("AUTHENTICATION FAILED")
					return render_template('login.html')	
		else:
			flash("AUTHENTICATION FAILED")
			return render_template('login.html')
	return render_template('login.html')
#app.logger.info(un)
@app.route('/logout')
def logout():
	session.clear()
	return render_template('logout.html')
@app.route('/change',methods=['GET','POST'])
def change():
	if request.method=='POST':
		old_p=request.form['old_password']
		new_p=sha256_crypt.encrypt(str(request.form['new_password']))
		cur=mysql.connection.cursor()
		us=cur.execute("SELECT * FROM users WHERE username=%s",[un])
		pas=cur.fetchone()['password']
		if sha256_crypt.verify(old_p,pas):
			cur.execute("UPDATE users SET password=%s WHERE username=%s",[new_p,un])
			mysql.connection.commit()
			cur.close()
			return render_template('user_home.html',name=un)
		else:
			flash("OLD PASSWORD DOENT MATCH!!")
			return render_template('change.html',name=un)
	return render_template('change.html',name=un)
@app.route('/user_home')
def user_home():
	return render_template('user_home.html',name=un)
@app.route('/change_user',methods=['GET','POST'])
def change_user():
	if request.method=='POST':
		p=request.form['password']
		ns=request.form['new_user']
		cur=mysql.connection.cursor()
		us=cur.execute("SELECT * FROM users WHERE username=%s",[un])
		pas=cur.fetchone()['password']
		if sha256_crypt.verify(p,pas):
			cur.execute("UPDATE users SET username=%s WHERE password=%s",[ns,pas])
			global un
			un=ns
			mysql.connection.commit()
			cur.close()
			return render_template('user_home.html',name=un)
		else:
			flash("PASSWORD DOENT MATCH!!")
			return render_template('change_user.html',name=un)
	return render_template('change_user.html',name=un)
if __name__=='__main__':
	app.secret_key=("secretkey")
	app.debug=True
	app.run()
