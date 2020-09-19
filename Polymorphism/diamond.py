class A:
    def method(self):
        print("Class A")

class B(A):
    pass

class C(A):
    def method(self):
        print("Class C")

class D(B,C):
    pass

d1 = D()
d1.method()
