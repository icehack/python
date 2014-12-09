def tailrecursive(f):
    call = True
    recurring = False
    def wrapper(*args):
        nonlocal call, recurring
        if recurring:
            recurring = False
            call = True
            return args
        while call:
            call = False
            recurring = True
            args = f(*args)
        call = True
        recurring = False
        return args
    return wrapper

'''
e.g.

def factorial(n):
    @tailrecursive
    def aux(v, acc):
        return acc if v <= 1 else aux(v - 1, v * acc)
    return aux(n, 1)
'''
