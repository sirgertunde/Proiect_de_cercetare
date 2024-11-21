import math

from hybrid_gcd_algorithm import binary_gcd, binary_gcd_bitwise_version, hybrid_gcd, hybrid_gcd_bitwise
from known_gcd_algorithms import euclid_gcd, extended_euclid_gcd


def test_euclid_gcd():
    a = 1234567890
    b = 9876543210
    assert euclid_gcd(a, b) == math.gcd(a, b)


def test_extended_euclid_gcd():
    a = 1234567890
    b = 9876543210
    assert extended_euclid_gcd(a, b) == math.gcd(a, b)


def test_binary_gcd():
    a = 1234567890
    b = 9876543210
    assert binary_gcd(a, b) == math.gcd(a, b)


def test_binary_gcd_bitwise_version():
    a = 1234567890
    b = 9876543210
    assert binary_gcd_bitwise_version(a, b) == math.gcd(a, b)


def test_hybrid_gcd():
    a = 1234567890
    b = 9876543210
    assert hybrid_gcd(a, b) == math.gcd(a, b)


def test_hybrid_gcd_bitwise():
    a = 1234567890
    b = 9876543210
    assert hybrid_gcd_bitwise(a, b) == math.gcd(a, b)


def run_tests():
    test_hybrid_gcd()
    test_binary_gcd_bitwise_version()
    test_binary_gcd()
    test_euclid_gcd()
    test_extended_euclid_gcd()
    test_hybrid_gcd_bitwise()
    print("Tests passed!")
