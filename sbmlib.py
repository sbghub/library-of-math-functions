# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:57:22 2015

@author: Somak
"""
'''
library of functions for these puzzles
'''

def hmti(a, b): #how many times b goes into a?
    if type(a)!=int or type(b)!=int: return "type error"
    if b==0: return "divide by zero error"
    elif b==1: return "infinite"
    if a%b==0:
        i=0
        while a%b==0:
            a=a/b
            i+=1
        return i
    else:
        if a>b:
            return 1
        else:
            return 0

def isprime(n): #is n prime?
    if type(n)!=int: return False
    if n<3:
        if n==2: return True
        else: return False
    elif n%2==0: return False
    else:
        cap, i = n**.5, 3
        while i <= cap:
            if n%i==0: return False
            i += 2
        return True
    
def rotateleft(s): #rotate string to the left
    if type(s)!=str: return "type error"
    s += s[0]
    s = s[1:]
    return s

def prime(n): #what is the nth prime?
    if type(n)!=int: return "type error"
    if n==1: return 2
    else:
        x = 1
        while n>1:
            x += 2
            prime = True
            cap, i = x**.5, 3
            while i <= cap: #dont count if prime
                if x%i==0: 
                    prime = False
                    break
                i += 2
            if prime==True: n -= 1
        return x

def circprime(p): #is p a circular prime
    if type(p)!=int: return False
    p = str(p)
    for n in p:
        if isprime(int(p))==False:
            return False
        p = rotateleft(p)
    return True

def primefactors(n): #what are the prime factors of n?
    if type(n)!=int: return "type error"
    P = 3
    x = []
    while n%2==0: #eliminate the evenness, check if 2 is factor
        if 2 not in x: x.append(2)
        n = n/2
    while P<=n:        
        while n%P==0: #check all other possible prime factors
            if P not in x: x.append(P)
            n = n/P
        P += 2
    return x
        
def exsamedigits(a, b): #are the digits in each number the same jumbled
    a, b = sorted(list(str(a))), sorted(list(str(b)))
    if a==b: return True
    else: return False        

def factorial(n): #factorial of given number
    if type(n)!=int: return "type error"
    x = 1
    while n > 1:
        x = x * n
        n -= 1
    return x

def fibn(n): #fibonacci
    if type(n)!=int: return "type error"
    a, b = 0, 1
    while n>0:
        a, b = b, a+b
        n -= 1
    return a    

def sumofdigits(n):
    if type(n)!=int: return "type error"
    s = 0
    while n>9:
        s, n = s + n%10, n/10
    s = s+n
    return s

def numFactors(x):
    if type(x)!=int: return "type error"
    i, count = 1, 0

    while i<=(x**.5):
        if x%i==0: 
            count += 2
        i += 1

    return count