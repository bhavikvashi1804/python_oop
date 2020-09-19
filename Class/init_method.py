class Student:
    
    def __init__(self,name):
        self.name= name

    def displayStudentDetails(self):
        print("Student name",self.name)

studentOne = Student("Bhavik Vashi")
studentOne.displayStudentDetails()

studentTwo = Student("Raj Patel")
studentTwo.displayStudentDetails()