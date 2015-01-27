def tailrecursive(f):
    recurring = False
    def wrapper(*args):
        nonlocal recurring
        if recurring:
            recurring = False
            return args
        while not recurring:
            recurring = True
            args = f(*args)
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
