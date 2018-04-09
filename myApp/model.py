from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests
from app import *

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

