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
def hmti(a, b):
    if type(a) != int or type(b) != int:
        return "type error"
    if b == 0:
        return "divide by zero error"
    elif b == 1:
        return "infinite"
    if a % b == 0:
        i = 0
        while a % b == 0:
            a = a / b
            i += 1
        return i
    else:
        return "not divisible"


# (2.) lets you know if n is prime
def isprime(n):
    if type(n) != int:
        return False
    if n < 3:
        if n == 2:
            return True
        else:
            return False
    elif n % 2 == 0:
        return False
    else:
        cap, i = n**.5, 3
        while i <= cap:
            if n % i == 0:
                return False
            i += 2
        return True


# (3.) rotate string to the left by a character
def rotateleft(s):
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
def circprime(p):
    if type(p) != int:
        return False
    p = str(p)

    for n in p:
        if not isprime(int(p)):
            return False
        p = rotateleft(p)

    return True


# (6.) what are the prime factors of n?
def primefactors(n):
    if type(n) != int:
        return "type error"
    P = 3
    x = []
    if isprime(n):
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


def factorial(n):
    if type(n) != int:
        return "type error"
    x = 1
    while n > 1:
        x = x * n
        n -= 1
    return x


# (9.) find the nth fibonacci number
def fibn(n):
    if type(n) != int:
        return "type error"
    elif n < 0:
        return "index out of bounds"
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a


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
    def test_hmtl(self):
        self.assertEqual(hmti(15, 3), 1)
        self.assertEqual(hmti(15, 2), 0)
        self.assertEqual(hmti(9, 3), 2)

    def test_isprime(self):
        self.assertEqual(isprime(-1), False)
        self.assertEqual(isprime(7), True)
        self.assertEqual(isprime(2), True)
        self.assertEqual(isprime(.5), False)

    def test_sumofdigits(self):
        self.assertEqual(sumofdigits(12345), 15)

    def test_numFactors(self):
        self.assertEqual(numFactors(121), 2)
        self.assertEqual(numFactors(113), 1)
        self.assertEqual(numFactors(6), 3)


if __name__ == '__main__':
    unittest.main()
