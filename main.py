#-----------------------------------------
# main2.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
nav = Nav()
nav.register_element('top', Navbar(
    View('Home', 'index'),View('About', 'about'),
    View('Books', 'books'), View('Publishers','publishers'),View('Authors','authors')))
app = Flask(__name__)
nav.init_app(app)
Bootstrap(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/books/')
def books():
	return render_template('books.html')

@app.route('/publishers/')
def publishers():
	return render_template('publishers.html')

@app.route('/authors/')
def authors():
	return render_template('authors.html')

if __name__ == "__main__":
	app.run()
#----------------------------------------
# end of main2.py
#-----------------------------------------