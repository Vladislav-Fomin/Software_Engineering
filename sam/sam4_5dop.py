from math import sqrt
def heron_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return None
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s