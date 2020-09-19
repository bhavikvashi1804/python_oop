class Employee:
    noOfWorkingHours = 8


employeeOne = Employee()
print("Emp 1: No of working hours: " + str(employeeOne.noOfWorkingHours) )

employeeTwo = Employee()
print("Emp 2: No of working hours: " + str(employeeTwo.noOfWorkingHours) )

#lets change the value of class attribute
Employee.noOfWorkingHours=10
print("After changing the value of class attribute, lets check the value of class attribute in both object")
print("Emp 1: No of working hours: " + str(employeeOne.noOfWorkingHours) )
print("Emp 2: No of working hours: " + str(employeeTwo.noOfWorkingHours) )