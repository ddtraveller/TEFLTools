import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def print_query_results(cursor):
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print()

print("PostgreSQL Basics Demonstration")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    user="your_username",
    password="your_password"
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

# Create a new database
db_name = "school"
cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
print(f"Database '{db_name}' created.")

# Connect to the new database
conn.close()
conn = psycopg2.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database=db_name
)
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE,
        birth_date DATE,
        gpa NUMERIC(3,2)
    )
""")
print("Table 'students' created.")

# Insert data
cursor.execute("""
    INSERT INTO students (name, email, birth_date, gpa)
    VALUES (%s, %s, %s, %s)
""", ('John Doe', 'john@example.com', '2000-01-15', 3.75))

cursor.execute("""
    INSERT INTO students (name, email, birth_date, gpa)
    VALUES (%s, %s, %s, %s)
""", ('Jane Smith', 'jane@example.com', '1999-05-20', 3.90))

print("Data inserted into 'students' table.")

# Update data
cursor.execute("""
    UPDATE students SET gpa = %s WHERE name = %s
""", (3.80, 'John Doe'))
print("Data updated in 'students' table.")

# Basic SELECT queries
print("\nAll students:")
cursor.execute("SELECT * FROM students")
print_query_results(cursor)

print("Students with GPA > 3.8:")
cursor.execute("SELECT name, gpa FROM students WHERE gpa > 3.8")
print_query_results(cursor)

print("Students ordered by GPA:")
cursor.execute("SELECT name, gpa FROM students ORDER BY gpa DESC")
print_query_results(cursor)

# Delete data
cursor.execute("DELETE FROM students WHERE name = %s", ('John Doe',))
print("Data deleted from 'students' table.")

print("\nRemaining students:")
cursor.execute("SELECT * FROM students")
print_query_results(cursor)

# Clean up
conn.close()

print("This script demonstrated basic PostgreSQL operations including:")
print("1. Connecting to PostgreSQL")
print("2. Creating a database and table")
print("3. Inserting, updating, and deleting data")
print("4. Performing basic SELECT queries")