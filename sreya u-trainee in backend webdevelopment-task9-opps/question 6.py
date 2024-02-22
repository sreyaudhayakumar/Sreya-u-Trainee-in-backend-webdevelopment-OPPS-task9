# 6) Extend the above solution and add another instance attribute called grade (should be string). 
# Assign value to grade from within the constructor.
# The value should not be taken from user input.
# Instead use the following conditions and assign values to grade by using the value of score.
# grade = A+ if score >=90
# grade = A if score >=80 and <90
# grade = B+ if score >=70 and <80
# and so on.
# if score is below 40 then grade should be "FAILED"


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        if score >= 90:
            self.grade = "A+"
        elif score >= 80:
            self.grade = "A"
        elif score >= 70:
            self.grade = "B+"
        elif score >= 60:
            self.grade = "B"
        elif score >= 50:
            self.grade = "C"
        elif score >= 40:
            self.grade = "D"
        else:
            self.grade = "FAILED"
            
name=str(input("enter the name:"))
score=int(input("enter the score:"))

student1 = Student(name, score)

print("Name of student: ", student1.name)
print("Score of student : ", student1.score)
print("Grade of student: ", student1.grade)