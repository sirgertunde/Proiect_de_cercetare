from time import perf_counter_ns


def euclid_gcd(a, b):
    """
    :param a: cryptographically large number
    :param b: cryptographically large number
    :return: the greatest common divisor of a and b using the Euclidean algorithm
    """
    t = perf_counter_ns()
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r
    elapsed_time = perf_counter_ns() - t
    print("Euclidean algorithm in " + str(elapsed_time) + " seconds")
    return a


def extended_euclid_gcd(a, b):
    """
        :param a: cryptographically large number
        :param b: cryptographically large number
        :return: the greatest common divisor of a and b using the Extended Euclidean algorithm
        """
    t = perf_counter_ns()
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
    elapsed_time = perf_counter_ns() - t
    #print(f"Extended Euclidean algorithm in {(elapsed_time / 1000000000):.8f} seconds")
    print("Extended Euclidean algorithm in " + str(elapsed_time) + " nanoseconds")
    return a
