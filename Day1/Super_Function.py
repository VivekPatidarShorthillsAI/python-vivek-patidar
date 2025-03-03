class Parent:
    def display(self):
        print("Parent method")

class Child(Parent):
    def display(self):
        super().display()  # Calling Parent method
        print("Child method")

c = Child()
c.display()
# Output: Parent method