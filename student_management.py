"""
Student Registration System — CLI-based student record manager.

Single-file by design (see README): a fundamentals exercise covering
OOP, exception handling, and JSON-based file persistence.
"""

import json

DATA_FILE = "stud.json"

students = []


class Student:
    """A single student record."""

    def __init__(self, student_id, name, dept, cgpa):
        self.student_id = student_id
        self.name = name
        self.dept = dept
        self.cgpa = cgpa

    def display(self):
        """Print this student's details."""
        print(f"\nID: {self.student_id}")
        print(f"NAME: {self.name}")
        print(f"DEPARTMENT: {self.dept}")
        print(f"CGPA: {self.cgpa}\n")

    def to_dict(self):
        """Serialize this student to a plain dict for JSON storage."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "dept": self.dept,
            "cgpa": self.cgpa,
        }


def add_student():
    """Prompt for a new student's details and save them."""
    try:
        student_id = int(input("ENTER THE STUDENT ID: "))
        for student in students:
            if student.student_id == student_id:
                print("Student ID already exists")
                return
        name = input("ENTER THE NAME OF THE STUDENT: ")
        dept = input("ENTER THE DEPARTMENT: ")
        cgpa = float(input("ENTER THE CGPA: "))
    except ValueError:
        print("ID and CGPA must be numbers")
        return

    student = Student(student_id, name, dept, cgpa)
    students.append(student)
    save_student()


def save_student():
    """Persist the in-memory student list to the JSON data file."""
    data = [student.to_dict() for student in students]
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_students():
    """Load students from the JSON data file, if it exists."""
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        for record in data:
            student = Student(
                record["student_id"],
                record["name"],
                record["dept"],
                record["cgpa"],
            )
            students.append(student)
    except (FileNotFoundError, json.JSONDecodeError):
        pass


def view_students(student_list):
    """Print every student in the given list."""
    if not student_list:
        print("No student data found")
        return
    for student in student_list:
        student.display()


def search_student():
    """Search for a student by ID and print their details."""
    if not students:
        print("No student data found")
        return
    try:
        search_id = int(input("Enter ID to search: "))
    except ValueError:
        print("ID must be a number")
        return

    for student in students:
        if search_id == student.student_id:
            student.display()
            return
    print("Student not found")


def update_student():
    """Find a student by ID and update their details."""
    if len(students) == 0:
        print("NO STUDENT DATA FOUND")
        return
    try:
        stud_id = int(input("Enter the student ID to update: "))
    except ValueError:
        print("ID must be a number")
        return

    for student in students:
        if student.student_id == stud_id:
            try:
                new_id = int(input("ENTER THE NEW ID: "))
                for other in students:
                    if other != student and new_id == other.student_id:
                        print("This student ID already exists")
                        return
                student.student_id = new_id
                student.name = input("ENTER THE NEW NAME: ")
                student.dept = input("ENTER THE NEW DEPARTMENT: ")
                student.cgpa = float(input("ENTER THE NEW CGPA: "))
                save_student()
            except ValueError:
                print("ID & CGPA must be numbers")
            return
    print("Student not found")


def delete_student():
    """Find a student by ID and remove them."""
    if len(students) == 0:
        print("NO STUDENT DATA FOUND")
        return
    try:
        stud_id = int(input("Enter the student ID to delete: "))
    except ValueError:
        print("ID must be a number")
        return

    for student in students:
        if student.student_id == stud_id:
            students.remove(student)
            save_student()
            print("Student successfully deleted")
            return
    print("Student not found")


def main():
    """Run the menu-driven CLI loop."""
    load_students()

    while True:
        print("--User Menu--")
        print(
            "1.add_student \n 2.view_student \n 3.search_student \n "
            "4.Update_student \n 5.Delete_student \n 6.Exit"
        )
        try:
            choice = int(input("Enter your choice 1 or 2 or 3 or 4 or 5 or 6: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students(students)
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            print("BYE!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
