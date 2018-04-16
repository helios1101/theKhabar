from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import *





#db = SQLAlchemy()
'''
db1 = create_engine('mysql://root:#Neel1998@localhost/myapp')
db2 = create_engine('mysql://root:aarush123@@localhost/NEWS')
DB1 = sessionmaker(db1)
DB2 = sessionmaker(db2)
db1session = DB1()
db2session = DB2()
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


class Likes(db.Model):

	__tablename__ = "Likes"

	uid = db.Column(db.Integer,primary_key=True,autoincrement=True)
	news = db.Column(db.String(length =300,convert_unicode =True),nullable = False)
	user = db.Column(db.String(length=30))
	likes=db.Column(db.Integer)

	def __init__(self,news,username,likes):
		self.news=news
		self.user=username
		self.likes=likes




class Views(db.Model):

	__tablename__ = "Views"

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
	url = db.Column(db.Text)
	description = db.Column(db.Text)
	image = db.Column(db.Text)
	keyword = db.Column(db.String(30))

	def __init__(self,title,author,date,summary,url,description,image,keyword):
		self.title = title
		self.author = author
		self.date = date
		self.summary = summary
		self.url = url
		self.description =description
		self.image = image
		self.keyword = keyword

		

class Sports(News,db.Model):
	
	__tablename__ = "Sports"
	

	def __init__(self,title,author,date,summary,url,description,image,keyword):
		News.__init__(self,title,author,date,summary,url,description,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }
	
class General(News,db.Model):
	
	__tablename__ = "General"
	

	def __init__(self,title,author,date,summary,url,description,image,keyword):
		News.__init__(self,title,author,date,summary,url,description,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }

class Science(News,db.Model):
	
	__tablename__ = "Science"
	

	def __init__(self,title,author,date,summary,url,description,image,keyword):
		News.__init__(self,title,author,date,summary,url,description,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }

class Business(News,db.Model):
	
	__tablename__ = "Business"
	

	def __init__(self,title,author,date,summary,url,description,image,keyword):
		News.__init__(self,title,author,date,summary,url,description,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }


class Technology(News,db.Model):
	
	__tablename__ = "Technology"
	

	def __init__(self,title,author,date,summary,url,description,image,keyword):
		News.__init__(self,title,author,date,summary,url,description,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }

class Entertainment(News,db.Model):
	
	__tablename__ = "Entertainment"
	

	def __init__(self,title,author,date,summary,url,description,image,keyword):
		News.__init__(self,title,author,date,summary,url,description,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }

class Health(News,db.Model):
	
	__tablename__ = "Health"
	

	def __init__(self,title,author,date,summary,url,description,image,keyword):
		News.__init__(self,title,author,date,summary,url,description,image,keyword)

	__mapper_args__ = {
        'concrete': True
    }



