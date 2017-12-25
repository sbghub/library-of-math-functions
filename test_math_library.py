import unittest
from math_library import (
    int_input,
    choose,
    circular_prime,
    collatz_sequence,
    consecutive_prime_sum,
    digit_sum,
    distinct_prime_factors,
    factorial,
    factor_list,
    fibonacci,
    goldbach_pair,
    is_prime,
    largest_prime_factor,
    least_common_multiple,
    lexicographic_permutation,
    multiple_of,
    nth_prime,
    palindrome,
    triangular_number,
    truncatable_prime)


class MathLibraryTest(unittest.TestCase):
    def test_choose(self):
        self.assertEqual(choose(3.2, 1), "Please enter an integer")
        self.assertEqual(choose(5, 3), 10)
        self.assertEqual(choose(23, 10), 1144066)

    def test_circular_prime(self):
        self.assertEqual(circular_prime("ninety-seven"), "Please enter an integer")
        self.assertTrue(circular_prime(97))
        self.assertFalse(circular_prime(23))
        self.assertTrue(circular_prime(37))
        self.assertFalse(circular_prime(45))

    def test_collatz_sequence(self):
        self.assertTrue(isinstance(collatz_sequence(2), list))
        self.assertEqual(collatz_sequence(13), [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(collatz_sequence(0), "please enter a positive integer")
        self.assertEqual(collatz_sequence(1), [1])

    def test_consecutive_prime_sum(self):
        self.assertEqual(consecutive_prime_sum(41), 6)
        self.assertEqual(consecutive_prime_sum(953), 21)
        self.assertEqual(consecutive_prime_sum(60), 4)
        self.assertEqual(consecutive_prime_sum(36), 4)
        self.assertFalse(consecutive_prime_sum(35))

    def test_digit_sum(self):
        self.assertEqual(digit_sum(123), 6)
        self.assertEqual(digit_sum(1000000000), 1)
        self.assertEqual(digit_sum(125435), 20)
        self.assertEqual(digit_sum(-124), 7)

    def test_distinct_prime_factors(self):
        self.assertEqual(distinct_prime_factors(14), [2, 7])
        self.assertEqual(distinct_prime_factors(15), [3, 5])
        self.assertEqual(distinct_prime_factors(644), [2, 7, 23])
        self.assertEqual(distinct_prime_factors(645), [3, 5, 43])
        self.assertEqual(distinct_prime_factors(646), [2, 17, 19])

    def test_factor_list(self):
        self.assertEqual(factor_list(5.5), "Please enter an integer")
        self.assertEqual(factor_list(-1), "Please enter a positive integer")
        self.assertTrue(factor_list(23), list)
        self.assertEqual(factor_list(4), [1, 2, 4])
        self.assertEqual(factor_list(23), [1, 23])
        self.assertEqual(factor_list(12), [1, 2, 3, 4, 6, 12])
        self.assertEqual(factor_list(28), [1, 2, 4, 7, 14, 28])
        self.assertEqual(factor_list(45), [1, 3, 5, 9, 15, 45])

    def test_factorial(self):
        self.assertEqual(factorial(0.1), "Please enter an integer")
        self.assertEqual(factorial(-1), "Please enter a non-negative integer")
        self.assertEqual(factorial("0"), 1)
        self.assertEqual(factorial(0), factorial(1.0))
        self.assertEqual(factorial("wone"), "Please enter an integer")
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci('two'), 'Please enter an integer')
        self.assertEqual(fibonacci(-1), 'Please enter a positive integer')
        self.assertEqual(fibonacci('5'), 5)
        self.assertEqual(fibonacci(3.0), 2)

    def test_goldbach_pair(self):
        self.assertTrue(goldbach_pair(9), (7, 1))
        self.assertTrue(goldbach_pair(15), (13, 1))

    def test_int_input(self):
        @int_input
        def test_func(number):
            return isinstance(number, int)

        self.assertTrue(test_func(1.0))
        self.assertEqual(test_func(1.0001), "Please enter an integer")
        self.assertTrue(test_func("1.0"))
        self.assertEqual(test_func("wone"), "Please enter an integer")
        self.assertTrue(test_func(-2))

    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(15))
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(29.0))
        self.assertFalse(is_prime(145.0))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-1))
        self.assertEqual(is_prime('twenty three'), 'Please enter an integer')

    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor('twenty three'), 'Please enter an integer')
        self.assertEqual(largest_prime_factor(29), 'Please enter a non-prime integer greater than 1')
        self.assertEqual(largest_prime_factor(0), 'Please enter a non-prime integer greater than 1')
        self.assertEqual(largest_prime_factor(28), 7)
        self.assertEqual(largest_prime_factor(10), 5)
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(128), 2)

    def test_least_common_multiple(self):
        self.assertEqual(least_common_multiple([5, 10, 15]), 30)
        self.assertEqual(least_common_multiple([2, 4, 6, 8]), least_common_multiple([8, 3]))

    def test_lexicographic_permutation(self):
        self.assertTrue(isinstance(lexicographic_permutation("01", 1), str))
        self.assertEqual(lexicographic_permutation("01", 1), "01")
        self.assertEqual(lexicographic_permutation("01", 2), "10")
        self.assertEqual(lexicographic_permutation("012", 1), "012")
        self.assertEqual(lexicographic_permutation("012", 3), "102")
        self.assertEqual(lexicographic_permutation("012", 4), "120")
        self.assertEqual(lexicographic_permutation("012", 6), "210")
        self.assertEqual(lexicographic_permutation(210, 6), "012")

    def test_multiple_of(self):
        self.assertTrue(multiple_of("15.0", [3, 5]))
        self.assertTrue(multiple_of(15, [3, 5]))
        self.assertTrue(multiple_of(-4, 2))
        self.assertTrue(multiple_of(9.0, 3))
        self.assertEqual(multiple_of(9.1, 3), 'Please enter an integer and a list of factors')
        self.assertFalse(multiple_of(9, 2))
        self.assertEqual(multiple_of('nine', 3), 'Please enter an integer and a list of factors')

    def test_nth_prime(self):
        self.assertEqual(nth_prime(-2), 'Please enter a positive integer')
        self.assertEqual(nth_prime(6.1), 'Please enter an integer')
        self.assertEqual(nth_prime(0), 'Please enter a positive integer')
        self.assertEqual(nth_prime('six'), 'Please enter an integer')
        self.assertEqual(nth_prime(1.0), 2)
        self.assertEqual(nth_prime(2), 3)
        self.assertEqual(nth_prime(6), 13)
        self.assertEqual(nth_prime(6), 13)

    def test_palindrome(self):
        self.assertTrue(palindrome(101))
        self.assertFalse(palindrome(100))
        self.assertTrue(palindrome(1001))
        self.assertTrue(palindrome('10101'))
        self.assertFalse(palindrome('please enter an integer'))
        self.assertTrue(palindrome('amanaplanacanalpanama'))

    def test_triangular_number(self):
        self.assertEqual(triangular_number(-1), "Please enter a positive integer")
        self.assertEqual(triangular_number(1), 1)
        self.assertEqual(triangular_number(5), 15)
        self.assertEqual(triangular_number(7), 28)

    def test_truncatable_prime(self):
        self.assertFalse(truncatable_prime(1234))
        self.assertTrue(truncatable_prime(3797))
        self.assertTrue(truncatable_prime(37))
        self.assertTrue(truncatable_prime(797))
        self.assertFalse(truncatable_prime(3))


if __name__ == '__main__':
    unittest.main()
