def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b != 0:
        return a/b
    else:
        raise ValueError('На ноль делить нельзя! ')

def check(num):
    return num % 2 == 0
