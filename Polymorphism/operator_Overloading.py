class square:
    def __init__(self,side):
        self.side=side

    def __add__(self,s1):
        return ((4*self.side) + (4*s1.side))

square1 = square(5)
square2 = square(10)

print("Sum of two square is", square1+square2)
