class Grandparent:
    def method_gp(self):
        print("Grandparent Method")

class Parent(Grandparent):
    def method_p(self):
        print("Parent Method")

class Child(Parent):
    def method_c(self):
        print("Child Method")

c = Child()
c.method_gp()  # Output: Grandparent Method
c.method_p()   # Output: Parent Method
c.method_c()   # Output: Child Method
