# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:57:22 2015

@author: Somak
"""
'''
library of mathematical functions for puzzles that weren't in numpy
probably my favorite personal library
the function names are weird since this is one of the first things I started making and I've used this library so much
'''

 
#(1.) returns how many times b goes into a 
def hmti(a, b): 
    
    #checks to makes sure 
    #1. you're taking in two integers
    #2. that you're not trying to see how many times 0 goes into a number (it doesn't)
    #3. that it returns infinite for how many times 1 goes into a number
    
    if type(a)!=int or type(b)!=int: return "type error"
    if b==0: return "divide by zero error"
    elif b==1: return "infinite"
    
    #increments i for however many times a can be divided by b if a can be divided by b at all
    #otherwise tells you a cannot be divided by b
    
    if a%b==0:
        i=0
        while a%b==0:
            a=a/b
            i+=1
        return i
    else:
        return "not divisible"

    

#(2.) lets you know if n is prime
def isprime(n):
    
    #returns False if n isn't an integer, since only integers can be prime
    
    if type(n)!=int: return False
    
    #Handles zero, negative integers, and even integers, 
    #basically eliminates 3/4 of integers
    #since 2 is the only even prime and the only prime less than 3
    
    #This leaves n only if it's an odd, positive integer
    
    if n<3:
        if n==2: return True
        else: return False
    elif n%2==0: return False
    
    #you only have to check odd factors < 3 and >= square root of n for minimal processing
    #each distinct factor of n greater than n's square root has exactly 1 corresponding distinct factor less than n's square root
    
    else:   
        cap, i = n**.5, 3
        while i <= cap:
            if n%i==0: return False
            i += 2
        
        #prime if it's 2 or an odd number with no odd factors below or equal to its square root
        #for example, every odd number between 3 and 119 that isn't divisible by 3, 5, or 7 must be prime (except 3, 5, and 7 of course)
        #this function would check for divisibility by 9 even though it's redundant
        
        return True


#(3.) rotate string to the left by a character
#e.g. 'string' becomes 'trings'

#odd one out, but convenient for circprime() below

def rotateleft(s): 
    # checks if s is a string
    if type(s)!=str: return "type error"
    # adds the first letter to the end
    s += s[0]
    # removes the first letter and returns the string 
    s = s[1:]
    return s


#(4.) what is the nth prime?

def prime(n):
    
    #returns error messages if n isn't a positive integer and handles 2 for n=1, since it's the only even prime
    
    if type(n)!=int: return "type error"
    if n==1: return 2
    elif n<1 return "index out of bounds"
    else:
        x = 1
        
        #n = number of primes to tally, not including 2
        #keeps running through primes as long as there's more than 1 prime left to check for
        
        while n>1:
            
            #increases x by 2 at the beginning of each runthrough in case this x is the last prime to look for
            #assumes x is prime until proven otherwise
            
            x += 2
            prime = True
            
            #only checks odd factors < 3 and >= square root of n for minimal processing
            #since each distinct factor of n greater than n's square root has exactly 1 corresponding factor less than n's square root
            
            cap, i = x**.5, 3
            while i <= cap:
                
                #breaks out of the loop and turns 'prime' false if x is divisible by an odd factor between 3 and x's square root
                #which would make it clearly not prime
                
                if x%i==0: 
                    prime = False
                    break
                i += 2
            
            #decrements n every time x isn't disproven to be prime
            
            if prime==True: n -= 1
        
        #returns the last prime number after n has been reduced to 1, since n=1 returns 2 before the loop
        
        return x


#(5.) is p a circular prime?
#A circular prime is a number that is prime for every rotation of its digits
#e.g. 113 is a circular prime since 113, 131, and 311 are all prime
#167 isn't since 716 is a rotation that clearly isn't

def circprime(p): 
    
    #returns False for non-integer values of p since only integers can be prime
    #then converts p to a string
    
    if type(p)!=int: return False
    p = str(p)
    
    #first, check if p is prime
    #then for each digit in p, rotate p by a digit and check if the result number is prime
    
    for n in p:
        
        #return False if p or any of it's rotations aren't prime
        
        if isprime(int(p))==False:
            return False
        p = rotateleft(p)
    
    #return True if p and all it's rotations are prime
    
    return True


#(6.) what are the prime factors of n?

def primefactors(n): 
    
    #returns an error message if n isn't an integer since only integers can be factored
    
    if type(n)!=int: return "type error"
    
    #initializes the (currently empty) list of factors and the first odd prime factor to check divisibility for
    
    P = 3
    x = []
    
    #if n is prime, then it's it's only prime factor and this function has done its job
    
    if isprime(n)==True:
        x.append(n)
        return x
    
    #if n is even then 2 gets included in the list of prime factors and n gets divided by 2 until it isn't anymore
    
    while n%2==0:
        if 2 not in x: x.append(2)
        n = n/2
    
    #if n is divisible by P, then P gets included in the list of prime factors and n gets divided by P until it isn't
    #this goes on until P is greater than n, with P incrementing by 2
    #When P > n, the list of distinct prime factors is full and can be returned
    
    while P<=n:        
        while n%P==0: #check all other possible prime factors
            if P not in x: x.append(P)
            n = n/P
        P += 2
    return x


#(7.) do a and b have the exact same digits?

def exsamedigits(a, b): 
    
    #makes a sorted list for the stringified characters in a and b
    #returns True if they match and False if they don't
    #says digits in the function name, but can take strings and floats
    
    a, b = sorted(list(str(a))), sorted(list(str(b)))
    if a==b: return True
    else: return False        


#(8.) factorial of n
#decided not to do it through recursion
#wasn't as fast when timed

def factorial(n): 
    
    #checks if n is an integer before going
    #returns error if it isn't
    
    if type(n)!=int: return "type error"
    
    #starts x off as 1, then sets it equal to x*n until n=1, with n decrementing by 1
    #returns x once n=1
    
    x = 1
    while n > 1:
        x = x * n
        n -= 1
    return x


#(9.) find the nth fibonacci number

def fibn(n):
    
    #returns an error message if n isn't a positive integer
    
    if type(n)!=int: return "type error"
    elif n<0: return "index out of bounds"
    
    #initializes a and b as the 0th and the 1st fibonacci numbers respectively
    #the puzzle I used this for didn't count 0 as the first one
    
    a, b = 0, 1
    
    #simultaneously sets a to b's current value and b to the sum of a and b's current values
    #effectively bumping both a and b to the next fibonacci numbers
    #then decrements n by 1
    #continues until n=0 at which point the nth fibonacci number is a
    
    while n>0:
        a, b = b, a+b
        n -= 1
    return a    


#(10.) find the sum of digits of integer n

def sumofdigits(n):
    
    #returns error message if n isn't an integer
    
    if type(n)!=int: return "type error"
    
    #initializes s as 0
    
    s = 0
    
    #while n has multiple digits,
    #s = s + (n mod 10 = n's last digiit) and n=n/10 making n = n without it's last digit since the result must remain an integer
    
    while n>9:
        s, n = s + n%10, n/10
    
    #once n has been reduced to one integer, it can just be added to s, making s = the sum of the digits n started out with
    
    s = s+n
    return s


#(11.) how many factors does x have?

def numFactors(x):
    
    #returns an error message if x isn't an integer
    
    if type(x)!=int: return "type error"
    
    #initialize count as 0 since x could be prime
    #and i as 2 since even prime numbers are divisible by 1
    
    i, count = 2, 0
    
    #check for all factors less than x's square root and increment count by 2 each time you find one
    #after all, every distinct factor of x less than its square root has exactly one factor greater than its square root
    
    while i<(x**.5):
        if x%i==0: 
            count += 2
        i += 1
    
    #of course if x's square root is one of its factors, then count should only increase by 1 when that factor's found
    #that would be the last factor to find and count can be returned at that point
    
    if i==x**.5: count += 1
    return count
