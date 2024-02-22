# 1)Write a program to create a class by name Students, and initialize attributes like name, age, 
# and grade while creating an object

class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
        
name=str(input("enter the name:"))
age=int(input("enter the age:"))
grade=(input("enter the grade:"))

stud_1=Student(name,age,grade)

print("Name: ", stud_1.name)
print("Age: ", stud_1.age)
print("Grade: ",stud_1.grade)
