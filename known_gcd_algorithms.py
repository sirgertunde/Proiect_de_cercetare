def euclid_gcd(a, b):
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def dijkstra_gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return dijkstra_gcd(a - b, b)
    else:
        return dijkstra_gcd(a, b - a)


def extended_euclidean_gcd(a, b):
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while b > 0:
        q = a // b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return a
