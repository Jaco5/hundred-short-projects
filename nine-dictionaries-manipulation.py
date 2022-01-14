#convert score integers to grade strings with same kets in new dict.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for i in student_scores:
    grade = ''
    if student_scores[i] > 90:
        grade = "Outstanding"
    elif student_scores[i] > 80:
        grade = "Exceeds Expectations"
    elif student_scores[i] > 70:
        grade = "Acceptable"
    else:   
        grade = "Fail"
    student_grades[i] = grade

print(student_grades)
