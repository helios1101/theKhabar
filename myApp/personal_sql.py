import MySQLdb
import MySQLdb.cursors 
from flask import Flask,jsonify
from app import *

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'	
app.config['MYSQL_PASSWORD']='aarush123@'
app.config['MYSQL_DB']='NEWS'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql=MySQL(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:aarush123@@localhost/NEWS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
db = SQLAlchemy(app)