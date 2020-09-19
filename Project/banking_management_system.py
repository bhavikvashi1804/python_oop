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
        print("Account creation has been successful. Your account number is ", self.accountNumber)
        print()
        
    def authUser(self,name, AC):
        print()
        if AC in self.savingAccounts.keys():
            if self.savingAccounts[AC][0] == name:
                self.accountNumber=AC
                print("Successfully Authenticated...")
                return True
            else:
                print("Authentication Fail: Check your name")
                return False
        else:
            print("Authentication Fail: We can't found any account with this AC no")
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
        
    def checkBalance(self):
        print("Avaliable balance: {} INR".format(self.savingAccounts[self.accountNumber][1]) )
        


savingsAccount = SavingAccount()
while True:
    print()
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    userChoice = int(input())
    print()
    if userChoice is 1:
        print()
        print("Enter your name: ")
        name = input()
        print("Enter the initial deposit: ")
        deposit = int(input())
        savingsAccount.createNewAC(name,deposit)
        print()
    elif userChoice is 2:
        print()
        print("Enter your name: ")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        authenticationStatus = savingsAccount.authUser(name, accountNumber)
        print()
        if authenticationStatus is True:
            while True:
                print()
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display avialable balance")
                print("Enter 4 to go back to the previous menu")
                userChoice = int(input())
                print()
                if userChoice is 1:
                    print()
                    print("Enter a withdrawal amount")
                    withdrawalAmount = int(input())
                    savingsAccount.withdraw(withdrawalAmount)
                    print()
                elif userChoice is 2:
                    print()
                    print("Enter an amount to be deposited")
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                    print()
                elif userChoice is 3:
                    print()
                    savingsAccount.checkBalance()
                    print()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
        quit()
