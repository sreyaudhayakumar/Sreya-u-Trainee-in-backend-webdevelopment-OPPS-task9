# 4) Write a program to create a child class Teacher that will inherit the properties from the parent class Staff.
#     attributes need for staff : role,department, salary
#     attributes need for teacher: name,age
#     method in  staff : def print_details()

#     output expected -
#         Name:  Raj
#         Age:  28
#         Role: Teacher
#         Department: Science

class Staff:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def details(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

class Teacher(Staff):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().details()

name = input("Enter the name: ")
age = int(input("Enter the age: "))
role = input("Enter the role: ")
department = input("Enter the department: ")
salary = float(input("Enter the salary: "))

teacher1 = Teacher(name, age, role, department, salary)
teacher1.print_details()
