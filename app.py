from flask import Flask
import os
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Connect to Postgresql database through my postgres user and .env password, returning the connection
def get_db_connection():
    conn = psycopg2.connect(dbname="YOUR_DATABASE_NAME", user="YOUR_USERNAME", host="localhost (most common) or an alternative host", password=os.environ.get('USER_PASSWORD'))
    return conn

# Open the database connection, perfoms and INSERT, UPDATE, DELETE action, etc., in the database and then close it when finished.
def execute_db_action(action, *values):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(action, (values))
    conn.commit()
    cur.close()
    conn.close()

# Import my routes from views.
from views import app