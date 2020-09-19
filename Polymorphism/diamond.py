class A:
    def method(self):
        print("Class A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass


