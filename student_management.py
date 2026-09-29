import pandas as pd
from database import load_students, save_students
from validation import validate_name, validate_age, validate_email

def add_student():
    df = load_students()
    student_id = input("Enter Student ID: ").strip()

    if student_id in df["student_id"].astype(str).values:
        print("Student ID already exists.")
        return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    email = input("Enter Email: ").strip()
    course = input("Enter Course: ").strip()

    if not validate_name(name):
        print("Invalid name.")
        return
    if not validate_age(age):
        print("Invalid age.")
        return
    if not validate_email(email):
        print("Invalid email.")
        return

    new_student = pd.DataFrame([{
        "student_id": student_id,
        "name": name,
        "age": int(age),
        "email": email,
        "course": course
    }])

    save_students(pd.concat([df, new_student], ignore_index=True))
    print("Student added successfully.")

def view_students():
    df = load_students()
    if df.empty:
        print("No students found.")
    else:
        print(df.to_string(index=False))

def search_student():
    df = load_students()
    student_id = input("Enter Student ID: ").strip()
    result = df[df["student_id"].astype(str) == student_id]

    if result.empty:
        print("Student not found.")
    else:
        print(result.to_string(index=False))

def update_student():
    df = load_students()
    student_id = input("Enter Student ID: ").strip()
    indexes = df.index[df["student_id"].astype(str) == student_id]

    if len(indexes) == 0:
        print("Student not found.")
        return

    i = indexes[0]

    name = input("New Name: ").strip()
    age = input("New Age: ").strip()
    email = input("New Email: ").strip()
    course = input("New Course: ").strip()

    if not validate_name(name) or not validate_age(age) or not validate_email(email):
        print("Invalid input.")
        return

    df.at[i, "name"] = name
    df.at[i, "age"] = int(age)
    df.at[i, "email"] = email
    df.at[i, "course"] = course

    save_students(df)
    print("Student updated successfully.")

def delete_student():
    df = load_students()
    student_id = input("Enter Student ID: ").strip()

    new_df = df[df["student_id"].astype(str) != student_id]

    if len(new_df) == len(df):
        print("Student not found.")
    else:
        save_students(new_df)
        print("Student deleted successfully.")
