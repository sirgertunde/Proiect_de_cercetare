def euclid_gcd(a, b):
    """
    :param a: cryptographically large number
    :param b: cryptographically large number
    :return: the greatest common divisor of a and b using the Euclidean algorithm
    """
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def extended_euclid_gcd(a, b):
    """
        :param a: cryptographically large number
        :param b: cryptographically large number
        :return: the greatest common divisor of a and b using the Extended Euclidean algorithm
        """
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
