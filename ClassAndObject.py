class Employee:
    def employeeDetails():
        pass

employeeOne=Employee()
employeeOne.employeeDetails()
# here it gives error because
# TypeError: employeeDetails() takes 0 positional arguments but 1 was given
# internally it calls Employee.employeeDetails(employeeOne)


