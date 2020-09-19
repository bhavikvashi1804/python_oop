class A:
    def method(self):
        print("Class A")

class B(A):
    def method(self):
        print("Class B")

class C(A):
    def method(self):
        print("Class C")

class D(C,B):
    pass

d1 = D()
d1.method()
