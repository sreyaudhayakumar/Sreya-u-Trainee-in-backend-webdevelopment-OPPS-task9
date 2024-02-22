# 5) Create a class named Student with name, score as instance attributes.
# Assign values to both of these attributes using a constructor.
# Create 2 Student objects. And also define a method called 'display' in the Student class -
# which, when called should print the name and score of the student.

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

name=str(input("enter the name:"))
score=int(input("enter the score:"))

student1 = Student(name,score)


print("Name: ", student1.name)
print("Score: ", student1.score)