class Employee:
    def setName(self):
        print("Set name method in parent class")
        self.name="Raj"
    
    def displayName(self):
        print(self.name)

class Trainee(Employee):
    def setName(self):
        print("Set name method in child class")
        self.name="Tranee: Raj"
   
    def setToEmp(self):
        super().setName()
        # super method is used to call the method of parent which has same in parent and child 



trainee1 = Trainee()
trainee1.setName()
print("Name:", end='')
trainee1.displayName()
print("After 6 months")
trainee1.setToEmp()
print("Name:", end='')
trainee1.displayName()