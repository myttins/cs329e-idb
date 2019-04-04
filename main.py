#-----------------------------------------
# main2.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from create_db import app, db, Book, Author, Publisher


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


@app.route('/publishers/')
def publishers():
	publishers = db.session.query(Publisher).all()
	return render_template('publishers.html', publishers = publishers)

@app.route('/authors/')
def authors():
	authors = db.session.query(Author).all()
	return render_template('authors.html', authors = authors)

import subprocess
@app.route('/test/')
def test():
    p = subprocess.Popen(["coverage", "run", "--branch", "test.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
    out, err = p.communicate()
    output=err+out
    output = output.decode("utf-8") #convert from byte type to string type
    
    return render_template('test.html', output = "<br/>".join(output.split("\n")))

if __name__ == "__main__":
	app.run()
#----------------------------------------
# end of main2.py
#-----------------------------------------