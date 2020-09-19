from abc import ABCMeta,abstractmethod
from random import randint

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
        self.accountNumber = randint(10000,99999)
        self.savingAccounts[self.accountNumber]=[name,initialDeposit]
        
    def authUser(self,name, AC):
        if AC in self.savingAccounts.keys():
            if self.savingAccounts[AC][0] == name:
                self.accountNumber=AC
                print("Successfully Authenticated...")
                return True
            else:
                print("Authentication Fail: Check your name")
                return False
        else:
            print("Authentication Fail: Check your AC number")
            return False

    def withdraw(self, amount):
        if amount > self.savingAccounts[self.accountNumber][1]:
            print("Insufficent Balance")
        else:
            self.savingAccounts[self.accountNumber][1] -= amount
            print("Money withdraw Successfully")
            print("Avaliable balance: {} INR".format(self.savingAccounts[self.accountNumber][1]) )

    def deposit(self, amount):
        self.savingAccounts[self.accountNumber][1] += amount
        print("Money Added Successfully")
        print("Avaliable balance: {} INR".format(self.savingAccounts[self.accountNumber][1]) )
        
    def checkBalance(self, amount):
        print("Avaliable balance: {} INR".format(self.savingAccounts[self.accountNumber][1]) )
        



