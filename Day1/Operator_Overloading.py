class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading `+` operator
        return Vector(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"Vector({self.x}, {self.y})")

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2  # Calls __add__ method
v3.display()  # Output: Vector(4, 6)
