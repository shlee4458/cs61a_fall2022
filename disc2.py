def make_keeper(n):
    def f(cond):
        k = 1
        while k <= n:
            if cond(k):
                print(k)
            k += 1
    return f

def is_even(x):
    return x % 2 == 0



def f1():
    """
    >>> f1()
    3
    """
    return lambda : 3

def f2():
    """
    >>> f2()()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda : lambda : 3

def f3():
    """
    >>> f3()(3)
    3
    """
    return lambda : lambda y : y

def f4():
    """
    >>> f4()()(3)()
    3
    """
    return lambda : lambda : lambda z : lambda : z



def match_k(k):
    def f(x):
        
        # if a digit and the pow(10,k) equates until 
        exp, i = k, 0
        while (x // pow(10, exp)) >= 1:
            if (x // pow(10, exp) % 10) != ((x // pow(10, i)) % 10):
                return False
            exp, i = exp + 1, i + 1
        return True
    return f