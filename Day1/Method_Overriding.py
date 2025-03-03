class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):  # Overriding the parent method
        print("This is Child class")

c = Child()
c.show()  # Output: This is Child class
