class A:
    def method(self):
        print("Class A")

class B(A):
    def method(self):
        print("Class B")

class C(A):
    pass

class D(B,C):
    pass

d1 = D()
d1.method()
