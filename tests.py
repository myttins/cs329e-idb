import os
import sys
import unittest
from models import db, Book
from create_db import db, Book, Author, Publisher

class DBTestCases(unittest.TestCase):
   
   def dummy_test(self):
       self.assertEqual(1,1)
   """ 

	class Book

	def test_source_Book_1(self):
		s = Book(id='100', title = 'Testing', isbn = "123")

		db.session.add(s)
		db.session.commit()

		r = db.session.query(Book).filter_by(id = '100').one()
		self.assertEqual(str(r.id), '100')

		db.session.query(Book).filter_by(id = '100').delete()
		db.session.commit()

	def test_source_Book_2(self):
		s = Book(id='101', title = 'Testing2', author = "Prachi Shah")

		db.session.add(s)
		db.session.commit()

		r = db.session.query(Book).filter_by(title = 'Testing2').one()
		self.assertEqual(str(r.author), 'Prachi Shah')

		db.session.query(Book).filter_by(id = '101').delete()
		db.session.commit()

	def test_source_Book_3(self):
		s = Book(id='102', title = 'Testing3', description = "This is a unit test")
		db.session.add(s)
		db.session.commit()

		r = db.session.query(Book).filter_by(id = '102').one()
		self.assertEqual(str(r.description), 'This is a unit test')

		db.session.query(Book).filter_by(id = '102').delete()
		db.session.commit()

   	class Author
	def test_source_Author_1(self):
   		s = Author(name = "Prachi", nationality = 'Indian')

   		db.session.add(s)
   		db.session.commit()

   		r = db.session.query(Author).filter_by(name = 'Prachi').one()
   		self.assertEqual(str(r.nationality), 'Indian')

   		db.session.query(Author).filter_by(name = 'Prachi').delete()
   		db.session.commit()

	def test_source_Author_2(self):
		s = Author(name = "Amaan", description = 'This is a unit test')

		db.session.add(s)
		db.session.commit()

		r = db.session.query(Author).filter_by(name = "Amaan").one()
		self.assertEqual(str(r.description), 'This is a unit test')

		db.session.query(Author).filter_by(name = 'Amaan').delete()
		db.session.commit()

	def test_source_Author_3(self):
		s = Author(name='Daniel', wikipedia_url= 'wikipedia.com')

		db.session.add(s)
		db.session.commit()

		r = db.session.query(Author).filter_by(name = 'Daniel').one()
		self.assertEqual(str(r.wikipedia_url), 'wikipedia.com')

		db.session.query(Author).filter_by(name = 'Daniel').delete()
		db.session.commit()


    class Publisher
	def test_source_Publisher_1(self):
		s = Publisher(name='Raza', location = 'Austin')
		
		db.session.add(s)
		db.session.commit()

		r = db.session.query(Publisher).filter_by(name = 'Raza').one()
		self.assertEqual(str(r.location), 'Austin')

		db.session.query(Publisher).filter_by(name = 'Raza').delete()
		db.session.commit()

	def test_source_Publisher_2(self):
		s = Publisher(name='Kevin', description="This is a unit test")

		db.session.add(s)
		db.session.commit()

		r = db.session.query(Publisher).filter_by(name='Kevin').one()
		self.assertEqual(str(r.description), 'This is a unit test')

		db.session.query(Publisher).filter_by(description = 'This is a unit test').delete()
		db.session.commit()

	def test_source_Publisher_3(self):
		s = Publisher(name='Prachi', website="test.com")

		db.session.add(s)
		db.session.commit()

		r = db.session.query(Publisher).filter_by(name='Prachi').one()
		self.assertEqual(str(r.website), 'test.com')

		db.session.query(Publisher).filter_by(name = 'Prachi').delete()
		db.session.commit()
"""
if __name__ == '__main__':
    unittest.main()


