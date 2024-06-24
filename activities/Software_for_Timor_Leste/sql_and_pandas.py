import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

print("SQL and Pandas Comparative Demonstration")

# Set up SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# 1. Creating Tables (SQL) and DataFrames (Pandas)
print("\n1. Creating Tables/DataFrames")

# SQL
cursor.execute('''
CREATE TABLE Students (
    sid CHAR(20) PRIMARY KEY,
    name VARCHAR(50),
    login VARCHAR(50),
    age INTEGER,
    gpa REAL
)
''')

# Pandas equivalent
students_data = {
    'sid': ['53666', '53688', '53650'],
    'name': ['Jones', 'Smith', 'Brown'],
    'login': ['jones@cs', 'smith@ee', 'brown@cs'],
    'age': [18, 20, 19],
    'gpa': [3.4, 3.8, 3.2]
}
df_students = pd.DataFrame(students_data)
print("Pandas DataFrame:")
print(df_students)

# 2. Inserting Data
print("\n2. Inserting Data")

# SQL
cursor.executemany('INSERT INTO Students VALUES (?,?,?,?,?)', [
    ('53666', 'Jones', 'jones@cs', 18, 3.4),
    ('53688', 'Smith', 'smith@ee', 20, 3.8),
    ('53650', 'Brown', 'brown@cs', 19, 3.2)
])
conn.commit()

# Pandas: Data is already in the DataFrame

# 3. Basic Queries
print("\n3. Basic Queries")

# SQL
print("SQL Query:")
cursor.execute('SELECT name, gpa FROM Students WHERE gpa > 3.5')
result = cursor.fetchall()
print(pd.DataFrame(result, columns=['name', 'gpa']))

# Pandas equivalent
print("\nPandas Query:")
print(df_students[df_students['gpa'] > 3.5][['name', 'gpa']])

# 4. Sorting
print("\n4. Sorting")

# SQL
print("SQL Sorting:")
cursor.execute('SELECT name, gpa FROM Students ORDER BY gpa DESC')
result = cursor.fetchall()
print(pd.DataFrame(result, columns=['name', 'gpa']))

# Pandas equivalent
print("\nPandas Sorting:")
print(df_students.sort_values('gpa', ascending=False)[['name', 'gpa']])

# 5. Joining Tables
print("\n5. Joining Tables")

# Create Courses table and DataFrame
cursor.execute('''
CREATE TABLE Courses (
    cid CHAR(20) PRIMARY KEY,
    title VARCHAR(100),
    credits INTEGER
)
''')
cursor.executemany('INSERT INTO Courses VALUES (?,?,?)', [
    ('CS101', 'Introduction to Computer Science', 3),
    ('EE200', 'Electric Circuits', 4),
    ('CS201', 'Data Structures', 4)
])

courses_data = {
    'cid': ['CS101', 'EE200', 'CS201'],
    'title': ['Introduction to Computer Science', 'Electric Circuits', 'Data Structures'],
    'credits': [3, 4, 4]
}
df_courses = pd.DataFrame(courses_data)

# Create Enrolled table and DataFrame
cursor.execute('''
CREATE TABLE Enrolled (
    studid CHAR(20),
    cid CHAR(20),
    FOREIGN KEY (studid) REFERENCES Students(sid),
    FOREIGN KEY (cid) REFERENCES Courses(cid)
)
''')
cursor.executemany('INSERT INTO Enrolled VALUES (?,?)', [
    ('53666', 'CS101'),
    ('53666', 'EE200'),
    ('53688', 'CS201'),
    ('53650', 'CS101')
])

enrolled_data = {
    'studid': ['53666', '53666', '53688', '53650'],
    'cid': ['CS101', 'EE200', 'CS201', 'CS101']
}
df_enrolled = pd.DataFrame(enrolled_data)

# SQL Join
print("SQL Join:")
cursor.execute('''
SELECT Students.name, Courses.title
FROM Students
INNER JOIN Enrolled ON Students.sid = Enrolled.studid
INNER JOIN Courses ON Enrolled.cid = Courses.cid
''')
result = cursor.fetchall()
print(pd.DataFrame(result, columns=['Student Name', 'Course Title']))

# Pandas equivalent
print("\nPandas Merge:")
df_merged = df_enrolled.merge(df_students, left_on='studid', right_on='sid')
df_merged = df_merged.merge(df_courses, on='cid')
print(df_merged[['name', 'title']])

# 6. Aggregation
print("\n6. Aggregation")

# SQL Aggregation
print("SQL Aggregation:")
cursor.execute('''
SELECT Courses.title, AVG(Students.gpa) as avg_gpa
FROM Students
INNER JOIN Enrolled ON Students.sid = Enrolled.studid
INNER JOIN Courses ON Enrolled.cid = Courses.cid
GROUP BY Courses.cid
''')
result = cursor.fetchall()
df_result = pd.DataFrame(result, columns=['Course Title', 'Average GPA'])
print(df_result)

# Pandas equivalent
print("\nPandas Aggregation:")
df_agg = df_merged.groupby('title')['gpa'].mean().reset_index()
df_agg.columns = ['Course Title', 'Average GPA']
print(df_agg)

# 7. Visualization (Pandas/Matplotlib)
print("\n7. Visualization")
plt.figure(figsize=(10, 6))
plt.bar(df_agg['Course Title'], df_agg['Average GPA'])
plt.title('Average GPA by Course')
plt.xlabel('Course')
plt.ylabel('Average GPA')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

conn.close()

print("\nThis script demonstrated the relationship between SQL operations and pandas functions,")
print("showing how data manipulation tasks can be performed in both SQL and pandas.")
print("It also incorporated data visualization, connecting to earlier lessons on data analysis.")