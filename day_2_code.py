#=========================Grading Program=============================#
# This is the scoring criteria:
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

def check_grade(score):
    if 90<score<101:
         return "Outstanding"
    elif 80<score<91:
         return "Exceeds Expectations"
    elif 70<score<81:
         return "Acceptable"
    else:
         return "Not Acceptable"

for key in student_scores:
     student_grades[key] = check_grade(student_scores[key])

print(student_grades)

#=================merge directory============================#
drc1 = {"a":1, "b":2, "c":3}
drc2 = {"d" : 4, "e" : 5, "f" : 6}

drc1.update(drc2)
print(f"{drc1}")
