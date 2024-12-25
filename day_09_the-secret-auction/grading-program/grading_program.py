student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for grades in student_scores:
    if 91 <= student_scores[grades] <= 100:
        student_grades[grades] = "Outstanding"
    elif 81 <= student_scores[grades] <= 90:
        student_grades[grades] = "Exceeds Expectations"
    elif 71 <= student_scores[grades] <= 80:
        student_grades[grades] = "Acceptable"
    else:
        student_grades[grades] = "Fail"
        
print(student_grades)