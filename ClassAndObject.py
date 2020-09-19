# Requirement: Create python program to check that employee has achieved target or not 
# create class 
class Employee:
    name="Bhavik Vashi"
    designation="Sales Executive"
    salesMadeInThisWeek=11
    def hasAchievedTarget(self):
        if self.salesMadeInThisWeek>10:
            print("Sales Target has been achieved")
        else:
            print("Sales Target has not been achieved")

# create object of class
# Creation of object is also called as object instantiation
employeeOne = Employee()
# access the attribute of object
print(employeeOne.name)
# call method for perticular object
employeeOne.hasAchievedTarget()