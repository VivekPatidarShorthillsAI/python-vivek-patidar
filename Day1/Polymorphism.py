class MathOperations:
    def add(self, a, b, c=0):  # Method overloading using default arguments
        return a + b + c

obj = MathOperations()
print(obj.add(2, 3))     # Output: 5
print(obj.add(2, 3, 4))  # Output: 9
