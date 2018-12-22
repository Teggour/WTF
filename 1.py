class Ch:
    def __getattr__(self, item):
        if item == "x":
            return '123'

        return '321'


ch = Ch()

a = ch.__getattr__('a')
print(a)

ch.abc = 123
print(ch.__dict__)

