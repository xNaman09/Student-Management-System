import matplotlib.pyplot as plt
from database import load_marks

def class_statistics():
    df = load_marks()

    if df.empty:
        print("No marks data available.")
        return

    print("Number of Students:", df["student_id"].nunique())
    print("Average Marks:", round(df["marks"].mean(), 2))
    print("Highest Marks:", df["marks"].max())
    print("Lowest Marks:", df["marks"].min())

def top_performers():
    df = load_marks()

    if df.empty:
        print("No marks data available.")
        return

    print(df.groupby("student_id")["marks"].mean().sort_values(ascending=False).head(5))

def performance_chart():
    df = load_marks()

    if df.empty:
        print("No marks data available.")
        return

    summary = df.groupby("student_id")["marks"].mean()
    summary.plot(kind="bar")
    plt.title("Student Performance")
    plt.xlabel("Student ID")
    plt.ylabel("Average Marks")
    plt.tight_layout()
    plt.show()
