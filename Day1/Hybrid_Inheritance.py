class A:
    def method_A(self):
        print("Method from Class A")

class B(A):  # Single Inheritance
    def method_B(self):
        print("Method from Class B")

class C(A):  # Another Single Inheritance
    def method_C(self):
        print("Method from Class C")

class D(B, C):  # Multiple Inheritance
    def method_D(self):
        print("Method from Class D")

obj = D()
obj.method_A()  # Output: Method from Class A
obj.method_B()  # Output: Method from Class B
obj.method_C()  # Output: Method from Class C
obj.method_D()  # Output: Method from Class D
