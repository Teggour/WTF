class X:
    def __get__(self, obj, cls=None):
        print(cls)
        print(obj)

        return 'ave'


class Z:
    x = X()


z = Z()

print(z.x)

print(Z.x)

