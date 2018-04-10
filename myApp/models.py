from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from newsapi import NewsApiClient as client  
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from app import *


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:aarush123@@localhost/NEWS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
db = SQLAlchemy(app)

#db = SQLAlchemy()
'''
db1 = create_engine('mysql://root:#Neel1998@localhost/myapp')
db2 = create_engine('mysql://root:aarush123@@localhost/NEWS')
DB1 = sessionmaker(db1)
DB2 = sessionmaker(db2)
db1session = DB1()
db2session = DB2()
'''
'''
class user(db.Model):
	__tablename__="userInfo"
	uid= db.Column(db.Integer,primary_key=True)
	name= db.Column(db.String(length=300),nullable=True)
	username= db.Column(db.String(length=300),nullable=True)
	email= db.Column(db.String(length=300),nullable=True)
	password= db.Column(db.String(length=300),nullable=True)
	def __init__(self,name,username,email,password):
		self.name=name
		self.username=username
		self.password=password
		self.email=email
'''

class Comments(db.Model):

	__tablename__ = "Comments"

	uid = db.Column(db.Integer,primary_key=True,autoincrement=True)
	news = db.Column(db.String(length =300,convert_unicode =True),nullable = False)
	user = db.Column(db.String(length=30))
	comments = db.Column(db.Text)

	def __init__(self,news,user='empty',comments='none'):
		self.news = news
		self.user = user
		self.comments = comments



class News:

	uid = db.Column(db.Integer,primary_key=True,autoincrement=True)
	title = db.Column(db.String(length =300,convert_unicode =True),nullable=False)
	author = db.Column(db.Text)
	date = db.Column(db.String(11))
	summary = db.Column(db.Text)
	image = db.Column(db.Text)
	keyword = db.Column(db.String(30))

	def __init__(self,title,author,date,summary,image,keyword):
		self.title = title
		self.author = author
		self.date = date
		self.summary = summary
		self.image = image
		self.keyword = keyword

		

class Sports(News,db.Model):
	
	__tablename__ = "Sports"
	

	def __init__(self,title,author,date,summary,image,keyword):
		News.__init__(self,title,author,date,summary,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }
	
class General(News,db.Model):
	
	__tablename__ = "General"
	

	def __init__(self,title,author,date,summary,image,keyword):
		News.__init__(self,title,author,date,summary,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }

class Science(News,db.Model):
	
	__tablename__ = "Science"
	

	def __init__(self,title,author,date,summary,image,keyword):
		News.__init__(self,title,author,date,summary,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }

class Buisness(News,db.Model):
	
	__tablename__ = "Buisness"
	

	def __init__(self,title,author,date,summary,image,keyword):
		News.__init__(self,title,author,date,summary,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }


class Technology(News,db.Model):
	
	__tablename__ = "Technology"
	

	def __init__(self,title,author,date,summary,image,keyword):
		News.__init__(self,title,author,date,summary,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }

class Entertainment(News,db.Model):
	
	__tablename__ = "Entertainment"
	

	def __init__(self,title,author,date,summary,image,keyword):
		News.__init__(self,title,author,date,summary,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }

class Health(News,db.Model):
	
	__tablename__ = "Health"
	

	def __init__(self,title,author,date,summary,image,keyword):
		News.__init__(self,title,author,date,summary,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }



