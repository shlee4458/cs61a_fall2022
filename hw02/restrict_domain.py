from math import sqrt

def restrict_domain(f, low_d, high_d):
    def h(x):
        if x > high_d:
            return float('-inf')
        elif x < low_d:
            return float('-inf')
        else:
            return f(x)
    return h