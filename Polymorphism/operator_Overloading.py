class square:
    def __init__(self,side):
        self.side=side

    def __add__(square1,square2):
        return ((4*square1.side) + (4*square2.side))

square1 = square(5)
square2 = square(10)

print("Sum of two square is", square1+square2)
