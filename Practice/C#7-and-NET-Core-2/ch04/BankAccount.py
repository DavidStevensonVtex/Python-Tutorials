from abc import ABC, abstractmethod


class AbstractBankAccount(ABC):
    @abstractmethod
    def pay_in(amount):
        pass

    @abstractmethod
    def withdraw(amount):
        pass

    @abstractmethod
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


class AbstractTransferBankAccount(AbstractBankAccount):
    @abstractmethod
    def transfer_to(destination: AbstractBankAccount, amount: float):
        pass


# TypeError: Can't instantiate abstract class CurrentAccount with abstract methods balance, pay_in, transfer_to, withdraw
class CurrentAccount(AbstractTransferBankAccount):
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

    def transfer_to(self, destination, amount):
        result = self.withdraw(amount)
        if result:
            destination.pay_in(amount)
        return result

    def __str__(self):
        return f"Jupiter Bank Saver: Balance = {self.__balance}"


# TypeError: Can't instantiate abstract class AbstractBankAccount with abstract methods balance, pay_in, withdraw
# aba = AbstractBankAccount()

current_account = CurrentAccount(2000)
print("After opening Jupiter account with $2000:", current_account)

sa = SaverAccount(500)
print("After opening Venus account with $500:", sa)

current_account.transfer_to(sa, 500)
print("After transfering $500 from Jupiter account to Venus account:", sa)
print("Jupiter account balance:", current_account)

# sa.pay_in(250)
# print("After $250 deposit: ", sa)

# success = sa.withdraw(125)
# print(f"Succesful withdrawal: {success}")
# print("After $125 withdrawal: ", sa)

# success = sa.withdraw(9999)
# print(f"Succesfull withdrawal: {success}")
# print("After $9999 withdrawal: ", sa)

# $ python BankAccount.py
# After opening account with $500:  Venus Bank Saver: Balance = 500
# After $250 deposit:  Venus Bank Saver: Balance = 750
# Succesful withdrawal: True
# After $125 withdrawal:  Venus Bank Saver: Balance = 625
# Withdrawal attempt failed.
# Succesfull withdrawal: False
# After $9999 withdrawal:  Venus Bank Saver: Balance = 625


# $ python BankAccount.py 
# After opening Jupiter account with $2000: Jupiter Bank Saver: Balance = 2000
# After opening Venus account with $500: Venus Bank Saver: Balance = 500
# After transfering $500 from Jupiter account to Venus account: Venus Bank Saver: Balance = 1000
# Jupiter account balance: Jupiter Bank Saver: Balance = 1500
