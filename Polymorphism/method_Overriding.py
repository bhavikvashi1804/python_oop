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
   
        

employee1 = Employee()
employee1.setName()
print("Name of Emp:", end='')
employee1.displayName()


trainee1 = Trainee()
trainee1.setName()
print("Name of Trainee:", end='')
trainee1.displayName()