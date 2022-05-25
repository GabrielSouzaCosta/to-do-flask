import os
import psycopg2

conn = psycopg2.connect(
    dbname="YOUR_DATABASE_NAME", 
    user="YOUR_USERNAME", 
    host="localhost (most common) or an alternative host", 
    password="PUT_YOUR_USER_PASSWORD_HERE_IF_NEEDED"
)
# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table named "todos"
cur.execute('DROP TABLE IF EXISTS items;')
cur.execute("""
        CREATE TABLE items (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            doing BOOLEAN NOT NULL DEFAULT FALSE,
            done BOOLEAN NOT NULL DEFAULT FALSE
        );
        """)

# Save changes and close
conn.commit()
cur.close()
conn.close()
