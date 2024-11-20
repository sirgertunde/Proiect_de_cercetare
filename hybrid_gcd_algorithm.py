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
