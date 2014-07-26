from random import randrange

def slowMinDiff(seq):
    dd = float("inf")
    for x in seq:
        for y in seq:
            if x == y: continue
            d = abs(x - y)
            if d < dd:
                xx, yy, dd = x, y, d
    return xx, yy

def fasterMinDiff(seq):
    dd = float("inf")
    seq.sort()
    for i in range(len(seq)-1):
        x, y = seq[i], seq[i+1]
        d = abs(x - y)
        if d < dd:
            xx, yy, dd = x, y, d
    return xx, yy

def testSlower():
    seq = [randrange(10**10) for i in range(100)]
    slowMinDiff(seq)

def testFaster():
    seq = [randrange(10**10) for i in range(100)]
    fasterMinDiff(seq)


if __name__ == '__main__':
    from timeit import timeit
    print timeit("testSlower()", setup="from __main__ import testSlower", number = 1)
    print timeit("testFaster()", setup="from __main__ import testFaster", number = 1)

