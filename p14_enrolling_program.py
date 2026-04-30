class Student:
    def __init__(self, name: str, email: str):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if "@" not in email:
            raise ValueError("Invalid email")

        self.name = name
        self.email = email

    def __str__(self):
        return f"Student Name: {self.name}, Email: {self.email}"


class Course:
    def __init__(self, course_name: str, max_students: int = 100):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []

    def enroll_student(self, student: Student):
        if len(self.students) >= self.max_students:
            print("Course is full.")
            return

        for current_student in self.students:
            if current_student.email.lower() == student.email.lower():
                print("Student already enrolled.")
                return

        self.students.append(student)
        print("Student enrolled successfully.")

    def view_students(self):
        if not self.students:
            print("No students enrolled.")
            return

        for student in self.students:
            print(student)

    def remove_student(self, email: str):
        for student in self.students:
            if student.email.lower() == email.lower():
                self.students.remove(student)
                print("Student removed successfully.")
                return

        print("Student not found.")

    def search_student(self, email: str):
        for student in self.students:
            if student.email.lower() == email.lower():
                print(student)
                return

        print("Student not found.")

    def available_seats(self):
        return self.max_students - len(self.students)

    def course_summary(self):
        print(f"Course: {self.course_name}")
        print(f"Enrolled: {len(self.students)}/{self.max_students}")
        print(f"Available Seats: {self.available_seats()}")

    def show_menu(self):
        while True:
            print("\n1. Enroll Student")
            print("2. View Students")
            print("3. Remove Student")
            print("4. Search Student")
            print("5. Available Seats")
            print("6. Course Summary")
            print("7. Exit")

            choice = input("Choose your option: ")

            if choice == "1":
                name = input("Enter student name: ")
                email = input("Enter student email: ")

                try:
                    student = Student(name, email)
                    self.enroll_student(student)
                except ValueError as error:
                    print(error)

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                email = input("Enter student email: ")
                self.remove_student(email)

            elif choice == "4":
                email = input("Enter student email: ")
                self.search_student(email)

            elif choice == "5":
                print(f"{self.available_seats()} seats available.")

            elif choice == "6":
                self.course_summary()

            elif choice == "7":
                print("Exiting program.")
                break

            else:
                print("Invalid input. Please try again.")


if __name__ == "__main__":
    course = Course("Python OOP", 3)
    course.show_menu()