import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STUDENT_FILE = os.path.join(BASE_DIR, "students.csv")
MARKS_FILE = os.path.join(BASE_DIR, "marks.csv")

def initialize_database():
    if not os.path.exists(STUDENT_FILE):
        pd.DataFrame(columns=["student_id", "name", "age", "email", "course"]).to_csv(STUDENT_FILE, index=False)
    if not os.path.exists(MARKS_FILE):
        pd.DataFrame(columns=["student_id", "subject", "marks"]).to_csv(MARKS_FILE, index=False)

def load_students():
    initialize_database()
    return pd.read_csv(STUDENT_FILE)

def save_students(df):
    df.to_csv(STUDENT_FILE, index=False)

def load_marks():
    initialize_database()
    return pd.read_csv(MARKS_FILE)

def save_marks(df):
    df.to_csv(MARKS_FILE, index=False)
