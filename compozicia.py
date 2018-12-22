class A:
    x = 1

    def __init__(self):
        print(self.x)
        super().__init__()


class B(A):
    def __init__(self):
        self.x = 2
        print(self.x)


class C(A):
    def __init__(self):
        self.x = 3
        print(self.x)


class D(B, C):
    def __init__(self):
        self.x = 4
        print(self.x)


a = A()

b = B()

c = C()

d = D()

print(D.mro())

