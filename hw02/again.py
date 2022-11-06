def again(f):
    n = 1
    while True:
        m = 0
        while m < n:
            if f(m) == f(n):
                return n
            m += 1
        n = n + 1

def parabola(x):
    """
    A parabola function (for testing the again function).
    """
    return (x-3) * (x-6)


def vee(x):
    return abs(x-2)


'''
compare f(m) and f(n)
increase n by one, loop until found an m
increase m by one until n-1
'''
