# beginning of models.py
# note that at this point you should have created "booksdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
import os
import pandas as pd

"""
initate flask application
"""
app = Flask(__name__)

"""
configure flask app to include postgres database
"""
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgresql://localhost/booksdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)



"""
create book class from corresponding database model
"""
class Book(db.Model):
	__tablename__ = 'book'

	"""
	initiate book id from first attribute
	"""
	id = db.Column(db.String(200))

	"""
	grab all other book information
	"""
	title = db.Column(db.String(80), nullable = False,primary_key = True)
	isbn=db.Column(db.Integer, nullable=False)
	publication_date=db.Column(db.String(2000))
	image_url=db.Column(db.String(200))
	description=db.Column(db.String(2000))
	publisher=db.Column(db.String(80),ForeignKey('publisher.name'))
	author=db.Column(db.String(80),ForeignKey('author.name'))

"""
create author class from corresponding database model
"""
class Author(db.Model):
	__tablename__ = 'author'

	"""
	add all information for authors
	"""
	name = db.Column(db.String(80),primary_key=True)
	nationality=db.Column(db.String(100))
	description=db.Column(db.String(2000))
	wikipedia_url=db.Column(db.String(200))
	image_url=db.Column(db.String(200))

	"""
	establish 1:1 relation
	"""
	books=db.relationship("Book")
	publisher=db.Column(db.String(200))


"""
create publisher class from corresponding database model
"""
class Publisher(db.Model):
	__tablename__ = 'publisher'
	
	"""
	grab all publisher information and insert into datbase
	"""
	name = db.Column(db.String(80), primary_key=True)
	location = db.Column(db.String(80))
	description=db.Column(db.String(2000))
	image_url=db.Column(db.String(200))
	wikipedia_url=db.Column(db.String(200))
	website=db.Column(db.String(200))
	author=db.Column(db.String(200))

	"""
	establish 1:many relation between book and publish
	""" 
	books=db.relationship("Book")



"""
launch database
"""
db.create_all()
