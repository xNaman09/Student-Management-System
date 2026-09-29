from database import initialize_database
from student_management import add_student, view_students, search_student, update_student, delete_student
from marks_management import add_marks, view_marks, calculate_result
from analytics import class_statistics, top_performers, performance_chart

def student_menu():
    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == "1": add_student()
        elif choice == "2": view_students()
        elif choice == "3": search_student()
        elif choice == "4": update_student()
        elif choice == "5": delete_student()
        elif choice == "6": break
        else: print("Invalid choice.")

def marks_menu():
    while True:
        print("\n===== MARKS MANAGEMENT =====")
        print("1. Add Marks")
        print("2. View Marks")
        print("3. Calculate Result")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1": add_marks()
        elif choice == "2": view_marks()
        elif choice == "3": calculate_result()
        elif choice == "4": break
        else: print("Invalid choice.")

def analytics_menu():
    while True:
        print("\n===== REPORTS & ANALYTICS =====")
        print("1. Class Statistics")
        print("2. Top Performers")
        print("3. Performance Chart")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1": class_statistics()
        elif choice == "2": top_performers()
        elif choice == "3": performance_chart()
        elif choice == "4": break
        else: print("Invalid choice.")

def main():
    initialize_database()

    while True:
        print("\n================================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Student Management")
        print("2. Marks & Results")
        print("3. Reports & Analytics")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1": student_menu()
        elif choice == "2": marks_menu()
        elif choice == "3": analytics_menu()
        elif choice == "4":
            print("Thank you for using the system.")
            break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
