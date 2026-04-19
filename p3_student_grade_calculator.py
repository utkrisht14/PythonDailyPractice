# Create a function calculate_average(marks):

def calculate_average() -> float:
    marks = []
    for i in range (5):
        input_marks = float(input(f"Enter the marks of subject-{i+1}: "))
        if input_marks < 0 or input_marks > 100:
            print("Invalid marks. Please enter marks between 0 and 100.")
            continue
        marks.append(input_marks)
    average_marks = sum(marks) / len(marks)
    return average_marks

def grade_average(marks: float) -> str:
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def display_result(name: str) -> None:
    student_marks = calculate_average()
    student_grade = grade_average(student_marks)
    print(
        f"Student: {name}, Marks: {student_marks}, Grade: {student_grade}"
    )


display_result("John")