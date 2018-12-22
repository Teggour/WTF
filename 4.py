class X:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.i = a

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.b:
            self.i += 1
            return self.i
        raise StopIteration
