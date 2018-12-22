def gen():
    print('pre')
    x = yield
    print('post', x)


g = gen()
next(g)
g.send('1')
next(g)
