import pandas as pd
from database import load_students, load_marks, save_marks
from validation import validate_marks

def add_marks():
    students = load_students()
    marks_df = load_marks()

    student_id = input("Enter Student ID: ").strip()

    if student_id not in students["student_id"].astype(str).values:
        print("Student not found.")
        return

    subject = input("Enter Subject: ").strip()
    marks = input("Enter Marks (0-100): ").strip()

    if not validate_marks(marks):
        print("Invalid marks.")
        return

    new_record = pd.DataFrame([{
        "student_id": student_id,
        "subject": subject,
        "marks": float(marks)
    }])

    save_marks(pd.concat([marks_df, new_record], ignore_index=True))
    print("Marks added successfully.")

def view_marks():
    df = load_marks()
    if df.empty:
        print("No marks found.")
    else:
        print(df.to_string(index=False))

def calculate_result():
    student_id = input("Enter Student ID: ").strip()
    df = load_marks()
    result = df[df["student_id"].astype(str) == student_id]

    if result.empty:
        print("No marks found.")
        return

    total = result["marks"].sum()
    percentage = total / len(result)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    status = "Pass" if percentage >= 40 else "Fail"

    print("\n----- RESULT -----")
    print("Student ID:", student_id)
    print("Total Marks:", total)
    print("Percentage:", round(percentage, 2))
    print("Grade:", grade)
    print("Status:", status)
