def div_rem(a,b):
    if b != 0:
        return a % b
    else:
        raise ValueError('На ноль делить нельзя! ')