def gcd(a,b):
    """greatest common divisor"""
    while a!=0:
        a,b = b%a, a
    return b

print(gcd(12,20))
