# Name: Harsh Chaudhary
# Roll no.: E22BCAU0029

class Shape:
    def _init_(self, color):
        self.color = color

    def area(self):
        pass

class Triangle(Shape):
    def _init_(self, base, height, color):
        Shape._init_(self, color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def _init_(self, radius, color):
        Shape._init_(self, color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

triangle = Triangle(10, 5, "red")
circle = Circle(7, "blue")

print("Triangle area: ", triangle.area())
print("Triangle color: ", triangle.color)
print("Circle area: ", circle.area())
print("Circle color: ", circle.color)
