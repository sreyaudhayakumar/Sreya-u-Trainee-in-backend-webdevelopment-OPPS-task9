# 7) Extend the above solution again and add another instance method called 'as_dict'.
# The method should return a dictionary with the data of the student.
# It should contain 'name', 'score', 'grade', keys and their respective values

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

    def as_dict(self):
        return {"name": self.name, "score": self.score, "grade": self.grade}

name=str(input("enter the name:"))
score=int(input("enter the score:"))

student1 = Student(name, score)

print("Student information: ", student1.as_dict())