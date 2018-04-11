from newsapi import NewsApiClient as client  
import requests,string
import newspaper 
from newspaper import Article as ar 
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


import MySQLdb as my
newsapi = client(api_key='b17240dd888f4069aa4cf3737c3df802')
top_headlines_sports =newsapi.get_top_headlines(
										category = 'sports',
										country = 'in',
										page_size = '100',
										)

top_headlines_business =newsapi.get_top_headlines(
										category = 'business',
										country = 'in',
										page_size = '100',
										)
top_headlines_general =newsapi.get_top_headlines(										
										category = 'general',
										country = 'in',
										page_size = '100',
										)
top_headlines_science =newsapi.get_top_headlines(
										category = 'science',
										country = 'in',
										page_size = '100',
										)
top_headlines_entertainment =newsapi.get_top_headlines(
										category = 'entertainment',
										country = 'in',
										page_size = '100',
										)
top_headlines_technology =newsapi.get_top_headlines(
										
										category = 'technology',
										country = 'in',
										page_size = '100',
										)

top_headlines_health =newsapi.get_top_headlines(
										
										category = 'health',
										country = 'in',
										page_size = '100',
										)

for article in top_headlines_sports['articles']:

	news = ar(article['url'])
	
	
	try:
		news.download()
		news.parse()
		news.nlp()
		for keyword in news.keywords:
			khabar = Sports(article['title'],article['author'],article['publishedAt'][0:10],news.summary,article['url'],article['description'],article['urlToImage'],keyword)
			
			db.session.add(khabar)
			db.session.commit()
	except newspaper.article.ArticleException:
		pass
	except:
		pass
		

for article in top_headlines_business['articles']:

	news = ar(article['url'])
	
	
	try:
		news.download()
		news.parse()
		news.nlp()
		
		for keyword in news.keywords:
			khabar = Business(article['title'],article['author'],article['publishedAt'][0:10],news.summary,article['url'],article['description'],article['urlToImage'],keyword)
			db.session.add(khabar)
			db.session.commit()
	except newspaper.article.ArticleException:
		pass
	except:
		pass
				

for article in top_headlines_entertainment['articles']:

	news = ar(article['url'])
	
	
	try:
		news.download()
		news.parse()
		news.nlp()
		for keyword in news.keywords:
			khabar = Entertainment(article['title'],article['author'],article['publishedAt'][0:10],news.summary,article['url'],article['description'],article['urlToImage'],keyword)
			db.session.add(khabar)
			db.session.commit()	
	except newspaper.article.ArticleException:
		pass
	except:
		pass
				

for article in top_headlines_science['articles']:

	news = ar(article['url'])
	
	
	try:
		news.download()
		news.parse()
		news.nlp()
		for keyword in news.keywords:
			khabar = Science(article['title'],article['author'],article['publishedAt'][0:10],news.summary,article['url'],article['description'],article['urlToImage'],keyword)
			db.session.add(khabar)
			db.session.commit()	
	except newspaper.article.ArticleException:
		pass
	except:
		pass
				

for article in top_headlines_general['articles']:

	news = ar(article['url'])
	
	
	try:
		news.download()
		news.parse()
		news.nlp()
		for keyword in news.keywords:
			khabar = General(article['title'],article['author'],article['publishedAt'][0:10],news.summary,article['url'],article['description'],article['urlToImage'],keyword)
			db.session.add(khabar)
			db.session.commit()	
	except newspaper.article.ArticleException:
		pass
	except:
		pass
				

for article in top_headlines_technology['articles']:

	news = ar(article['url'])
	
	
	try:
		news.download()
		news.parse()
		news.nlp()
		for keyword in news.keywords:
			khabar = Technology(article['title'],article['author'],article['publishedAt'][0:10],news.summary,article['url'],article['description'],article['urlToImage'],keyword)
			db.session.add(khabar)
			db.session.commit()	
	except newspaper.article.ArticleException:
		pass
	except:
		pass
			
for article in top_headlines_health['articles']:

	news = ar(article['url'])
	
	
	try:
		news.download()
		news.parse()
		news.nlp()
		for keyword in news.keywords:
			khabar = Health(article['title'],article['author'],article['publishedAt'][0:10],news.summary,article['url'],article['description'],article['urlToImage'],keyword)
			db.session.add(khabar)
			db.session.commit()	
	except newspaper.article.ArticleException:
		pass
	except:
		pass	
