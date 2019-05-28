'''
efficiency_with_mins.py defines two algorithms that each decide whether a number
is prime. The __main__ code times the algorithms and reports minimum times.

version 2/21/2014
Unpublished work (c) 2014 Project Lead The Way, Inc.
'''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
import timeit

def is_prime_versionA(number):
    """ Returns True if number is prime.
    Returns False otherwise.
    """
    # Refuse a very long execution time
    if number > 2**26: # # 2**26 is about 67,000,000
        return "That number is too big to run this algorithm quickly."
    
    # Refuse anything but positive integers
    if type(number) != int or number<1:
        return "That number is not a positive integer."
        
    # Initialize a one-way flag 
    prime = True
    
    # Check all possible divisors 
    # from 2 to number-1
    for possible_divisor in range(2, number-1):
        if number % possible_divisor == 0: 
            # No remainder, so it's a factor
            prime = False 

    return prime
    