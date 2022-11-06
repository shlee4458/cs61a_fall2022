def div_three(k):
    return k % 3 == 0

def div_five(k):
    return k % 5 == 0


def fizzbuzz(n):

    k = 1
    while k <= n:
        if div_three(k) and div_five(k):
            print("fizzbuzz")
        elif div_three(k):
            print("fizz")
        elif div_five(k):
            print("buzz")
        else:
            print(k)
        k += 1
