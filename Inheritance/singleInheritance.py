class Apple:
    manufacturer="Apple Inc."
    contactWebsite="www.apple.com/contact"

    def contactDetails(self):
        print("Visit us on:",self.contactWebsite)

class Macbook(Apple):
    def __init__(self):
        self.yearOfManufacture=2017
    def manufactureDetails(self):
        print("This MacBook is manufactured in {} by {}".format(self.yearOfManufacture,self.manufacturer))


macbook1 = Macbook()
macbook1.manufactureDetails()
macbook1.contactDetails()