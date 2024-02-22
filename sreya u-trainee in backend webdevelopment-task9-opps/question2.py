# 2)Write a program that prints the class name using its object.

class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
name=str(input("enter the name:"))
age=int(input("enter the age:"))

Teacher1 = Teacher(name,age)

print("Class Name: ", type(Teacher1).__name__)