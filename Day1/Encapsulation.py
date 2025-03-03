class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public Attribute
        self.__balance = balance  # Private Attribute (Encapsulation)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):  # Accessor method (getter)
        return self.__balance

# Creating object
account = BankAccount("12345", 5000)

print(account.account_number)  # Accessible
# print(account.__balance)  # Throws an error (Cannot access private attribute)

print(account.get_balance())  #  Accessing private variable via a method
