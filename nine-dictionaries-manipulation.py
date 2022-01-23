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

# More dictionary manipulation
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country,visits,cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities,
    })

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
