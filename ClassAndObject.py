class Employee:
    noOfWorkingHours = 8


employeeOne=Employee()
employeeTwo=Employee()

#create instance attribute
employeeOne.name = 'Bhavik Vashi'
print("Employee 1: name: " + str(employeeOne.name))
# print("Employee 2: name:" +  str(employeeTwo.name))
# At this point 
#this is instance attribute so you can not call employeeTwo.name

# so now lets create instance attribue for employeeTwo
employeeTwo.name = 'Raj Patel'
print("Employee 2: name: " +  str(employeeTwo.name))


#lets change the value of class attribute using emp object
employeeOne.noOfWorkingHours=10
print("Employee 1: Working hours: " + str(employeeOne.noOfWorkingHours))
print("Employee 2: Working hours: " + str(employeeTwo.noOfWorkingHours))
