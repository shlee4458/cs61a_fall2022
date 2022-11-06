def restrict_range(f, low_r, high_r):
    def h(x):
        if f(x) < low_r:
            return float("-inf") 
        elif f(x) > high_r:
            return float("-inf")
        else:
            return f(x)
    return h