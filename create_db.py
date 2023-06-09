import json
from models import app, db, Book, Author, Publisher
import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

temp = os.environ.get("DB_STRING", 'postgresql+psycopg2://postgres:password@/postgres?host=/cloudsql/cs-329e-website:us-central1:booksdb')
engine = create_engine(temp)
Base = declarative_base()
Base.metadata.create_all(engine)
file_name = 'books_only.csv'
df = pd.read_csv(file_name, encoding='latin-1')
df.to_sql(con=engine, index=False, index_label='id', name='book', if_exists='replace')


file_name = 'authors_only.csv'
df = pd.read_csv(file_name, encoding='latin-1')
df.to_sql(con=engine, index=False, index_label='name', name='author', if_exists='replace')

file_name = 'publishers_only.csv'
df = pd.read_csv(file_name, encoding='latin-1')
df.to_sql(con=engine, index=False, index_label='name', name='publisher', if_exists='replace')