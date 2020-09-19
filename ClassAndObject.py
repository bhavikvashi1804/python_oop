class Employee:
    def employeeDetails(self):
        self.name="Bhavik Vashi"
        # if you use self.variable then available for object
        # if you directly use variale then its scope is only inside method
        print("In Emp Details " + str(self.name))

employeeOne=Employee()
employeeOne.employeeDetails()
print("After exection of employeeDetails method")
print("Emp name: " + str(employeeOne.name))


