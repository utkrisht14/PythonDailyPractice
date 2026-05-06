class Person:
    def __init__(self, name, age):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if age <= 0:
            raise ValueError("Age must be greater than 0")

        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, grade, roll_number):
        super().__init__(name, age)
        self.grade = grade
        self.roll_number = roll_number

    def __str__(self):
        return f"{super().__str__()}, Grade: {self.grade}, Roll Number: {self.roll_number}"


class Teacher(Person):
    def __init__(self, name, age, subject, experience_years):
        super().__init__(name, age)
        self.subject = subject
        self.experience_years = experience_years

    def __str__(self):
        return f"{super().__str__()}, Subject: {self.subject}, Experience: {self.experience_years} years"


class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.teacher = None
        self.students = []

    def __len__(self):
        return len(self.students)

    def add_student(self, student: Student):
        for current_student in self.students:
            if current_student.roll_number == student.roll_number:
                raise ValueError("Student already exists in the classroom.")

        self.students.append(student)
        print("Student added to the classroom.")

    def assign_teacher(self, teacher: Teacher):
        self.teacher = teacher
        print("Teacher assigned successfully.")

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student

        return None

    def view_classroom(self):
        print(f"\nClassroom: {self.class_name}")

        if self.teacher:
            print(f"Teacher: {self.teacher}")
        else:
            print("Teacher: Not assigned")

        print("\nStudents:")
        if not self.students:
            print("No students added.")
            return

        for student in self.students:
            print(student)


teacher = Teacher("Mr. Sharma", 40, "Math", 10)

s1 = Student("Aman", 15, "10th", 1)
s2 = Student("Riya", 14, "10th", 2)

classroom = Classroom("10-A")
classroom.assign_teacher(teacher)
classroom.add_student(s1)
classroom.add_student(s2)

print(f"Total students: {len(classroom)}")
classroom.view_classroom()

found_student = classroom.search_student(1)
if found_student:
    print("\nFound Student:")
    print(found_student)
else:
    print("Student not found")