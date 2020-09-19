class Student:
    
    def enterStudentDetails(self):
        self.name= "Bhavik Vashi"

    def displayStudentDetails(self):
        print("Student name",self.name)

studentOne = Student()
studentOne.enterStudentDetails()
studentOne.displayStudentDetails()