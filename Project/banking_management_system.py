from abc import ABCMeta,abstractmethod

class Account(metaclass=ABCMeta):
    
    @abstractmethod
    def createNewAC(self):
        return 0
    @abstractmethod
    def authUser(self):
        return 0
    @abstractmethod
    def withdraw(self):
        return 0
    @abstractmethod
    def deposit(self):
        return 0
    @abstractmethod
    def checkBalance(self):
        return 0

        

class SavingAccount(Account):
    def __init__(self):
        self.savingAccounts={}

    def createNewAC(self, name , initialDeposit):
        pass
    def authUser(self,name, AC):
        pass
    def withdraw(self, amount):
        pass
    def deposit(self, amount):
        pass
    def checkBalance(self, amount):
        pass



