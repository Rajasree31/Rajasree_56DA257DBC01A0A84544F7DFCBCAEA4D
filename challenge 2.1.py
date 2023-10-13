# 2.1 Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"${amount} deposited. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"${amount} withdrawn. New balance: ${self.__account_balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive value."
        else:
            return "Insufficient balance for withdrawal."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance}"

# Create an instance of the BankAccount class
account = BankAccount("12345", "John Doe", 1000)

# Test deposit and withdrawal functionality
print(account.display_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(1500))