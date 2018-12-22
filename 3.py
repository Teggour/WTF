class A(int):
    def __new__(cls, x):
        return super().__new__(x*2)

print(A(2))
