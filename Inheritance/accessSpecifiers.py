# Public : variableName
# Protected : _variableName
# Private : __variableName

class Car:
    numberOfWheels=4
    _color="Black"
    __RCNo="GJ 16 AP 6738"

class Audi(Car):
    def __init__(self):
        print("Protected attribute",self._color)
        # print("Private attribute", self._RCNo)
        # pytho what does self._Car___RCNo
        # you cannot access private variable



audi1= Audi()
