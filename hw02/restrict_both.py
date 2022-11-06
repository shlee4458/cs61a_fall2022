from math import sqrt


def restrict_both(f, low_d, high_d, low_r, high_r):
    def h(x):
        if x < low_d or x > high_d or f(x) < low_d or f(x) > high_r:
            return float("-inf")
        else:
            return f(x)
        
    return h