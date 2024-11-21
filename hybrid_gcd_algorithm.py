def hybrid_gcd(a, b):
    """
        :param a: cryptographically large number
        :param b: cryptographically large number
        :return: the greatest common divisor of a and b
        combining the Euclidean and the Binary GCD algorithms
        """
    while max(a, b) > 2 ** 16:
        if b == 0:
            return a
        a, b = b, a % b
    return binary_gcd(a, b)


def hybrid_gcd_bitwise(a, b):
    """
        :param a: cryptographically large number
        :param b: cryptographically large number
        :return: the greatest common divisor of a and b
        combining the Euclidean and the Binary GCD algorithms
        """
    while max(a, b) > 2 ** 16:
        if b == 0:
            return a
        a, b = b, a % b
    return binary_gcd_bitwise_version(a, b)


def binary_gcd(a, b):
    """
        :param a: cryptographically large number
        :param b: cryptographically large number
        :return: the greatest common divisor of a and b using Stein's algorithm
        """
    if a == 0:
        return b
    if b == 0:
        return a
    if a % 2 == 0 and b % 2 == 0:
        return 2 * binary_gcd(a // 2, b // 2)
    elif a % 2 == 0:
        return binary_gcd(a // 2, b)
    elif b % 2 == 0:
        return binary_gcd(a, b // 2)
    else:
        return binary_gcd(abs(a - b) // 2, min(a, b))


def binary_gcd_bitwise_version(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    k = 0
    while ((a | b) & 1) == 0:
        a = a >> 1
        b = b >> 1
        k = k + 1
    while (a & 1) == 0:
        a = a >> 1
    while b != 0:
        while (b & 1) == 0:
            b = b >> 1
        if a > b:
            temp = a
            a = b
            b = temp
        b = (b - a)
    return a << k
