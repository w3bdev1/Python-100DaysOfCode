student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for name, marks in student_scores.items():
    if marks >= 91:
        student_grades[name] = "Outstanding"
    elif (marks >= 81) and (marks <= 90):
        student_grades[name] = "Exceeds Expectations"
    elif (marks >= 71) and (marks <= 80):
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)