class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment, grade):
        self.assignments[assignment] = grade

    def display_grades(self):
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student_id, assignment, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment, grade)
                print(f"Assigned {grade} to {student.name} for {assignment}")
                return
        print("Student not found.")

    def display_all_grades(self):
        for student in self.students:
            print(f"\n{student.name} ({student.student_id}):")
            student.display_grades()


# Interactive test
instructor = Instructor("Mr. Githogori", "Application Programming")
while True:
    print("\n1. Add Student\n2. Assign Grade\n3. View Grades\n4. Exit")
    choice = input("Select option: ")

    if choice == "1":
        name = input("Student name: ")
        sid = input("Student ID: ")
        student = Student(name, sid)
        instructor.add_student(student)
    elif choice == "2":
        sid = input("Student ID: ")
        assignment = input("Assignment: ")
        grade = input("Grade: ")
        instructor.assign_grade(sid, assignment, grade)
    elif choice == "3":
        instructor.display_all_grades()
    elif choice == "4":
        break
