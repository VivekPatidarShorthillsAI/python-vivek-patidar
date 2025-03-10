class OperatorsDemo:
    """
    A class demonstrating all types of operators in Python using OOP principles.
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def arithmetic_operators(self):
        print("\n--- Arithmetic Operators ---")
        print(f"Addition: {self.a} + {self.b} = {self.a + self.b}")
        print(f"Subtraction: {self.a} - {self.b} = {self.a - self.b}")
        print(f"Multiplication: {self.a} * {self.b} = {self.a * self.b}")
        print(f"Division: {self.a} / {self.b} = {self.a / self.b}")
        print(f"Floor Division: {self.a} // {self.b} = {self.a // self.b}")
        print(f"Modulus: {self.a} % {self.b} = {self.a % self.b}")
        print(f"Exponentiation: {self.a} ** {self.b} = {self.a ** self.b}")

    def comparison_operators(self):
        print("\n--- Comparison Operators ---")
        print(f"Equal: {self.a} == {self.b} -> {self.a == self.b}")
        print(f"Not Equal: {self.a} != {self.b} -> {self.a != self.b}")
        print(f"Greater Than: {self.a} > {self.b} -> {self.a > self.b}")
        print(f"Less Than: {self.a} < {self.b} -> {self.a < self.b}")
        print(f"Greater Than or Equal To: {self.a} >= {self.b} -> {self.a >= self.b}")
        print(f"Less Than or Equal To: {self.a} <= {self.b} -> {self.a <= self.b}")

    def logical_operators(self):
        print("\n--- Logical Operators ---")
        print(f"AND: ({self.a} > 0 and {self.b} > 0) -> {self.a > 0 and self.b > 0}")
        print(f"OR: ({self.a} > 0 or {self.b} > 0) -> {self.a > 0 or self.b > 0}")
        print(f"NOT: not({self.a} > 0) -> {not (self.a > 0)}")

    def bitwise_operators(self):
        print("\n--- Bitwise Operators ---")
        print(f"Bitwise AND: {self.a} & {self.b} = {self.a & self.b}")
        print(f"Bitwise OR: {self.a} | {self.b} = {self.a | self.b}")
        print(f"Bitwise XOR: {self.a} ^ {self.b} = {self.a ^ self.b}")
        print(f"Bitwise NOT: ~{self.a} = {~self.a}")
        print(f"Left Shift: {self.a} << 2 = {self.a << 2}")
        print(f"Right Shift: {self.a} >> 2 = {self.a >> 2}")

    def assignment_operators(self):
        print("\n--- Assignment Operators ---")
        x = self.a
        print(f"Initial value: x = {x}")
        x += self.b; print(f"x += {self.b} -> {x}")
        x -= self.b; print(f"x -= {self.b} -> {x}")
        x *= self.b; print(f"x *= {self.b} -> {x}")
        x /= self.b; print(f"x /= {self.b} -> {x}")
        x //= self.b; print(f"x //= {self.b} -> {x}")
        x %= self.b; print(f"x %= {self.b} -> {x}")
        x **= self.b; print(f"x **= {self.b} -> {x}")

    def identity_operators(self):
        print("\n--- Identity Operators ---")
        print(f"a is b: {self.a is self.b}")
        print(f"a is not b: {self.a is not self.b}")

    def membership_operators(self):
        print("\n--- Membership Operators ---")
        sample_list = [1, 2, 3, 4, 5]
        print(f"{self.a} in {sample_list}: {self.a in sample_list}")
        print(f"{self.b} not in {sample_list}: {self.b not in sample_list}")

if __name__ == "__main__":
    demo = OperatorsDemo(10, 3)
    demo.arithmetic_operators()
    demo.comparison_operators()
    demo.logical_operators()
    demo.bitwise_operators()
    demo.assignment_operators()
    demo.identity_operators()
    demo.membership_operators()
