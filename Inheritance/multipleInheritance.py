class OperatingSystem:
    multiTasking = True
    OS="MAC OS"

class Apple:
    website = "www.apple.com"
    OS="Apple OS"

class Macbook(OperatingSystem,Apple):

    def __init__(self):
        if(self.multiTasking is True):
            print("This is multitasking laptop, for more info visit us on  {} ".format(self.website))
            print(self.OS)
            # both parent class contains same attribute called OS
            # in order to access that variable it depends on order of inheritance
            # in your case Operating System is first
            # hence it takes OS value from Operating System Class

macbook1= Macbook()
