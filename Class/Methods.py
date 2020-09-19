class Employee:
    # Instance method
    def employeeDetails(self):
        self.name="Bhavik Vashi"

    # static method
    @staticmethod
    def welcomeMessage():
        # they do not need to access self parameter means attribute of object
        print("Welcome to GCET")


employeeOne= Employee()
employeeOne.employeeDetails()
print("Emp Name: ",employeeOne.name)
employeeOne.welcomeMessage()