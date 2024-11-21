from time import perf_counter_ns

from hybrid_gcd_algorithm import hybrid_gcd, binary_gcd_bitwise_version, hybrid_gcd_bitwise
from known_gcd_algorithms import euclid_gcd, extended_euclid_gcd
from tests import run_tests

if __name__ == "__main__":
    try:
        run_tests()
    except AssertionError:
        print("Tests did not pass")
    large_number1 = 139769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137210
    large_number2 = 139769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137300
    t = perf_counter_ns()
    gcd = euclid_gcd(large_number1, large_number2)
    print("Euclidean algorithm in " + str(perf_counter_ns() - t) + " nanoseconds")
    print(gcd)
    t = perf_counter_ns()
    gcd = extended_euclid_gcd(large_number1, large_number2)
    print("Extended Euclidean algorithm in " + str(perf_counter_ns() - t) + " nanoseconds")
    # print(f"Extended Euclidean algorithm in {(elapsed_time / 1000000000):.8f} seconds")
    print(gcd)
    t = perf_counter_ns()
    gcd = binary_gcd_bitwise_version(large_number1, large_number2)
    print("Binary GCD algorithm in " + str((perf_counter_ns() - t)) + " nanoseconds")
    print(gcd)
    t = perf_counter_ns()
    gcd = hybrid_gcd(large_number1, large_number2)
    print("Hybrid GCD algorithm in " + str((perf_counter_ns() - t)) + " nanoseconds")
    print(gcd)
    t = perf_counter_ns()
    gcd = hybrid_gcd_bitwise(large_number1, large_number2)
    print("Hybrid GCD algorithm with bitwise version in " + str((perf_counter_ns() - t)) + " nanoseconds")
    print(gcd)
