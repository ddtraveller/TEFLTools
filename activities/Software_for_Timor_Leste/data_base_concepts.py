import json

# Simulating a simple relational database structure
database = {
    "students": [
        {"student_id": 1, "name": "Alice", "age": 20},
        {"student_id": 2, "name": "Bob", "age": 22},
        {"student_id": 3, "name": "Charlie", "age": 21}
    ],
    "courses": [
        {"course_id": 101, "title": "Introduction to Python", "credits": 3},
        {"course_id": 102, "title": "Database Management", "credits": 4},
        {"course_id": 103, "title": "Web Development", "credits": 3}
    ],
    "enrollments": [
        {"enrollment_id": 1, "student_id": 1, "course_id": 101},
        {"enrollment_id": 2, "student_id": 1, "course_id": 102},
        {"enrollment_id": 3, "student_id": 2, "course_id": 101},
        {"enrollment_id": 4, "student_id": 3, "course_id": 103}
    ]
}

def print_table(table_name):
    print(f"\n{table_name.capitalize()} Table:")
    print(json.dumps(database[table_name], indent=2))

def query_student_courses(student_id):
    student = next((s for s in database["students"] if s["student_id"] == student_id), None)
    if not student:
        return f"Student with ID {student_id} not found."
    
    enrollments = [e for e in database["enrollments"] if e["student_id"] == student_id]
    courses = [next(c for c in database["courses"] if c["course_id"] == e["course_id"]) for e in enrollments]
    
    return f"Courses for {student['name']}:\n" + json.dumps(courses, indent=2)

# Demonstrate the database structure
print("Demonstrating a simple relational database structure:")
print_table("students")
print_table("courses")
print_table("enrollments")

# Demonstrate a simple query
print("\nDemonstrating a simple query:")
print(query_student_courses(1))

# Demonstrate adding a new record
print("\nAdding a new student:")
new_student = {"student_id": 4, "name": "David", "age": 23}
database["students"].append(new_student)
print_table("students")

# Demonstrate updating a record
print("\nUpdating a student's age:")
database["students"][0]["age"] = 21
print_table("students")

print("\nThis script demonstrates basic concepts of a relational database, including:")
print("1. Tables (students, courses, enrollments)")
print("2. Relationships (enrollments table links students and courses)")
print("3. Querying (finding courses for a specific student)")
print("4. Adding and updating records")