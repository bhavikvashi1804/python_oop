class MusicalInstruments:
    numberOfMajorKeys=12

class StringInstruments(MusicalInstruments):
    typeOfWood = "Tone wood"

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfString = 6
        print("This Guitar contains {} Strings. It is made of {} and it can play {} keys".format(self.numberOfString,self.typeOfWood,self.numberOfMajorKeys))
       

guitar1 = Guitar()