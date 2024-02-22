# 8) show class method, static method and instance method with simple example.


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * Circle.pi

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @staticmethod
    def is_valid_radius(radius):
        return radius > 0

radius = float(input("Enter the radius: "))
diameter = float(input("Enter the diameter: "))

circle1 = Circle(radius)

print("Area: ", circle1.area())

circle2 = Circle.from_diameter(diameter)

print("Radius: ", circle2.radius)

print("Valid Radius: ", Circle.is_valid_radius(radius))
print("Valid Radius: ", Circle.is_valid_radius(-radius))