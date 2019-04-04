#-----------------------------------------
# main2.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from create_db import app, db, Book, Author, Publisher
from models import app

nav = Nav()
nav.register_element('top', Navbar(
    View('Home', 'index'),View('About', 'about'),
    View('Books', 'books'), View('Publishers','publishers'),View('Authors','authors')))
nav.init_app(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/books/')
def books():
	books = db.session.query(Book).all()
	return render_template('books.html', books = books)

@app.route('/books/<title>')
def book_page(title):
	this_book=db.session.query(Book).filter_by(title=title).first()
	return render_template('eachbook.html', book=this_book)

@app.route('/authors/<name>')
def author_page(name):
	this_author=db.session.query(Author).filter_by(name=name).first()
	return render_template('eachauthor.html', author=this_author)

@app.route('/publishers/<name>')
def publisher_page(name):
	this_publisher=db.session.query(Publisher).filter_by(name=name).first()
	return render_template('eachpublisher.html', publisher=this_publisher)

@app.route('/publishers/')
def publishers():
	publishers=db.session.query(Publisher).all()
	return render_template('publishers.html', publishers=publishers)

@app.route('/authors/')
def authors():
	authors=db.session.query(Author).all()
	return render_template('authors.html', authors=authors)

@app.route('/test/')
def test():
	return render_template('test.html', test=test)


if __name__ == "__main__":
	app.debug=True
	app.run()
#----------------------------------------
# end of main2.py
#-----------------------------------------