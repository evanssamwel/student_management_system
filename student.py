import os

# Constants
WELCOME_MESSAGE = """
  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System ========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View Student's List
Enter 2 : To Add New Student
Enter 3 : To Search Student
Enter 4 : To Remove Student
"""

GOODBYE_MESSAGE = """
##############################################
#           Thank You For Using              #
#      Student Management System App         #
##############################################
"""

def display_students(students):
    """Display the list of students."""
    if not students:
        print("\nNo students found in the database.")
    else:
        print("\nList of Students:")
        for student in students:
            print(f"=> {student}")

def add_student(students):
    """Add a new student to the list."""
    new_student = input("Enter New Student Name: ").strip()
    if not new_student:
        print("\nStudent name cannot be empty.")
    elif new_student in students:
        print(f"\nStudent '{new_student}' is already in the database.")
    else:
        students.append(new_student)
        print(f"\nStudent '{new_student}' successfully added.")

def search_student(students):
    """Search for a student in the list."""
    search_name = input("Enter Student Name to Search: ").strip()
    if search_name in students:
        print(f"\nStudent '{search_name}' found in the database.")
    else:
        print(f"\nNo record found for student '{search_name}'.")

def remove_student(students):
    """Remove a student from the list."""
    remove_name = input("Enter Student Name to Remove: ").strip()
    if remove_name in students:
        students.remove(remove_name)
        print(f"\nStudent '{remove_name}' successfully removed.")
    else:
        print(f"\nNo record found for student '{remove_name}'.")

def manage_students():
    """Main menu for the student management system."""
    students = ["Kim", "Jenny", "Odhis", "Twatwai"]  # Initial list of students

    while True:
        print(WELCOME_MESSAGE)
        try:
            user_input = int(input("Please Select an Option: ").strip())
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 4.")
            continue

        if user_input == 1:
            display_students(students)
        elif user_input == 2:
            add_student(students)
        elif user_input == 3:
            search_student(students)
        elif user_input == 4:
            remove_student(students)
        else:
            print("\nInvalid option. Please try again.")

        run_again = input("\nDo you want to perform another operation? (Y/N): ").strip().lower()
        if run_again != 'y':
            print(GOODBYE_MESSAGE)
            break

if __name__ == "__main__":
    manage_students()
