# 3)Write a Python class, Square, and define two methods that return the square area and perimeter.

class Square:
    def __init__(self, length):
        self.length = length
        
    def area(self):
        print("Area of square is:", self.length ** 2)
        
    def perimeter(self):
        print("Perimeter of square is:", 4 * self.length)
        
Square_input = int(input("Enter the side length of the square: "))
        
square1 = Square(Square_input)

square1.area()
square1.perimeter()
