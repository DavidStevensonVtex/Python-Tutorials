from abc import ABC, abstractmethod


class AbstractBankAccount(ABC):
    def pay_in(amount):
        pass

    def withdraw(amount):
        pass

    def balance():
        pass


class SaverAccount(AbstractBankAccount):
    def __init__(self, balance):
        self.__balance = balance

    def pay_in(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            return True
        print("Withdrawal attempt failed.")
        return False

    def balance(self):
        return self.__balance

    def __str__(self):
        return f"Venus Bank Saver: Balance = {self.__balance}"


aba = AbstractBankAccount()

sa = SaverAccount(500)
print("After opening account with $500: ", sa)

sa.pay_in(250)
print("After $250 deposit: ", sa)

success = sa.withdraw(125)
print(f"Succesful withdrawal: {success}")
print("After $125 withdrawal: ", sa)

success = sa.withdraw(9999)
print(f"Succesfull withdrawal: {success}")
print("After $9999 withdrawal: ", sa)

# $ python BankAccount.py
# After opening account with $500:  Venus Bank Saver: Balance = 500
# After $250 deposit:  Venus Bank Saver: Balance = 750
# Succesful withdrawal: True
# After $125 withdrawal:  Venus Bank Saver: Balance = 625
# Withdrawal attempt failed.
# Succesfull withdrawal: False
# After $9999 withdrawal:  Venus Bank Saver: Balance = 625
