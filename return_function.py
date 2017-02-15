def count():
    fs = []
    for i in range(1, 4):
        def f(i):
             return i*i
        fs.append(f(i))
    return fs

def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

