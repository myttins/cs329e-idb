# beginning of models.py
# note that at this point you should have created "booksdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
import os
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgresql://localhost/booksdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

class Book(db.Model):
	__tablename__ = 'book'

	id = db.Column(db.Integer)
	title = db.Column(db.String(80), nullable = False,primary_key = True)
	isbn=db.Column(db.Integer, nullable=False)
	publication_date=db.Column(db.DateTime)
	image_url=db.Column(db.String(200))
	description=db.Column(db.String(2000))
	publisher=db.Column(db.String(80),ForeignKey('publisher.name'))
	author=db.Column(db.String(80),ForeignKey('author.name'))


class Author(db.Model):
	__tablename__ = 'author'

	name = db.Column(db.String(80),primary_key=True)
	nationality=db.Column(db.String(100))
	description=db.Column(db.String(2000))
	wikipedia_url=db.Column(db.String(200))
	image_url=db.Column(db.String(200))
	books=db.relationship("Book")


class Publisher(db.Model):
	__tablename__ = 'publisher'
	
	name = db.Column(db.String(80), primary_key=True)
	location = db.Column(db.String(80))
	description=db.Column(db.String(2000))
	image_url=db.Column(db.String(200))
	wikipedia_url=db.Column(db.String(200))
	website=db.Column(db.String(200))
	books=db.relationship("Book")


'''author_publishers = db.Table('author_publishers',
    db.Column('author_id', db.String(80), db.ForeignKey('author.name'), primary_key=True),
    db.Column('publisher_id', db.String(80), db.ForeignKey('publisher.name'), primary_key=True)
)'''


db.create_all()
