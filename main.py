#-----------------------------------------
# main2.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('hello.html')

@app.route('/books/')
def bookw():
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