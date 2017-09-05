#  -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:57:22 2015

@author: Somak
"""

import unittest

'''
library of mathematical functions for puzzles that weren't in numpy
probably my favorite personal library
the function names are weird since this is one of the first things I started making and I've used this library so much
'''


# (1.) returns how many times b goes into a
def how_many_times_in(numer, denom):
    if type(numer) != int or type(denom) != int:
        return "type error"
    if denom == 0:
        return "divide by zero error"
    elif denom == 1:
        return "infinite"
    if numer % denom == 0:
        i = 0
        while numer % denom == 0:
            numer = numer / denom
            i += 1
        return i
    else:
        return 0


# (2.) lets you know if n is prime
def is_prime(num):
    if type(num) != int:
        return False
    if num < 3:
        return num == 2
    elif num % 2 == 0:
        return False
    else:
        cap, incr = num**.5, 3
        while incr <= cap:
            if num % incr == 0:
                return False
            incr += 2
        return True


# (3.) rotate string to the left by a character
def rotate_left(s):
    if type(s) != str:
        return "type error"
    s += s[0]
    s = s[1:]
    return s


# (4.) what is the nth prime?
def prime(n):
    if type(n) != int:
        return "type error"
    if n == 1:
        return 2
    elif n < 1:
        return "index out of bounds"
    else:
        x = 1
        while n > 1:
            x += 2
            prime = True
            cap, i = x**.5, 3
            while i <= cap:
                if x % i == 0:
                    prime = False
                    break
                i += 2
            if prime:
                n -= 1
        return x


# (5.) is p a circular prime?
def circ_prime(p):
    p = str(p)
    for n in p:
        if not is_prime(int(p)):
            return False
        p = rotate_left(p)

    return True


# (6.) what are the prime factors of n?
def primefactors(n):
    if type(n) != int:
        return "type error"
    P = 3
    x = []
    if is_prime(n):
        x.append(n)
        return x
    while n % 2 == 0:
        if 2 not in x:
            x.append(2)
        n = n/2
    while P <= n:
        while n % P == 0:  # check all other possible prime factors
            if P not in x:
                x.append(P)
            n = n/P
        P += 2
    return x


# (7.) do a and b have the exact same digits?
def exsamedigits(a, b):
    a, b = sorted(list(str(a))), sorted(list(str(b)))
    if a == b:
        return True
    else:
        return False


# (8.) find the factorial of a number
def factorial(number):
    if type(number) != int:
        return "type error"
    incr = 1
    while number > 1:
        incr = incr * number
        number -= 1
    return incr


# (9.) find the nth fibonacci number
def fibonacci(index):
    if type(index) != int:
        return "type error"
    elif index < 0:
        return "index out of bounds"

    first, second = 0, 1
    while index > 0:
        first, second = second, first + second
        index -= 1
    return first


# (10.) find the sum of digits of integer n
def sumofdigits(n):
    if type(n) != int:
        return "type error"
    s = 0
    while n > 9:
        s, n = s + n % 10, n / 10
    s = s+n
    return s


# (11.) how many factors does x have?
def numFactors(x):
    if type(x) != int:
        return "type error"
    i, count = 2, 1
    while i < (x**.5):
        if x % i == 0:
            count += 2
        i += 1
    if i == x**.5:
        count += 1
    return count


class Tester(unittest.TestCase):
    def test_how_many_times_in(self):
        self.assertEqual(how_many_times_in(15, 3), 1)
        self.assertEqual(how_many_times_in(15, 2), 0)
        self.assertEqual(how_many_times_in(9, 3), 2)

    def test_is_prime(self):
        self.assertEqual(is_prime(-1), False)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(.5), False)

    def test_sumofdigits(self):
        self.assertEqual(sumofdigits(12345), 15)

    def test_numFactors(self):
        self.assertEqual(numFactors(121), 2)
        self.assertEqual(numFactors(113), 1)
        self.assertEqual(numFactors(6), 3)

    def test_circ_prime(self):
        self.assertEqual(circ_prime(17), True)
        self.assertEqual(circ_prime(29), False)

    def test_fibonacci(self):
        self.assertEquals(fibonacci(0), 0)
        self.assertEquals(fibonacci(1), 1)
        self.assertEquals(fibonacci(5), 5)
        self.assertEquals(fibonacci(7), 13)
        self.assertEquals(fibonacci(9), 34)


if __name__ == '__main__':
    unittest.main()
