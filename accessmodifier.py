class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
s = Student("Aswin", 23)
s.display()


# class BankAccount:
#     def __init__(self, account_number, balance):
#         self._account_number = account_number
#         self._balance = balance
#     def _display_balance(self):
#         print("Balance:", self._balance)

# b = BankAccount(1234567890, 1000)
# b._display_balance()  



# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number
#         self.__balance = balance

#     def __display_balance(self):
#         print("Balance:", self.__balance)

# b = BankAccount(1234567890, 5000)
# b._BankAccount__display_balance()  



class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def _display(self):
        print("Name:", self._name)
        print("Age:", self._age)

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self._roll_number = roll_number
    
    def display(self):
        self._display()
        print("Roll Number:", self._roll_number)
s = Student("Aswin", 23,27)
s.display()
