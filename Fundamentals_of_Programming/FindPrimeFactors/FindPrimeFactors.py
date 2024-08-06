# File: MinMax.py

# Description of Program: Program uses isPrime and isFindNextPrime to print out the prime factorizations of a number. Program uses input from the user to determine the prime factorizations. 

import math

def isPrime ( num ):

    if ( num < 2 or num % 2 == 0 ):
        return ( num == 2 )
    
    divisor = 3
    while ( divisor <= math . sqrt ( num )):
        if ( num % divisor == 0 ) :
            return False
        else :
            divisor += 2
    return True

def findNextPrime ( num ):
    num = num + 1

    while not isPrime(num):
        num = num + 1
    return num

def main():
    
    print("Find Prime Factors:")
    num = int(input("Enter a positive integer (or 0 to stop): "))
    while True:
        if num == 1:
            print("  1 has no prime factorization.")

        elif num == 0:
            print("Goodbye!")
            break

        elif num < 0:
            print("  Negative integer entered. Try again.")

        else: 
            inputNumber = num
            primeFactors = []

            if isPrime(num):
                primeFactors.append(num)

            else:
                primeFactors = []
                d = 2
                while num > 1:
                    while num % d == 0:
                        primeFactors.append(d)
                        num = num // d
                    d = findNextPrime(d)
            print("  The prime factorization of " + str(inputNumber) + " is: " + str(primeFactors))
        num = int(input("\nEnter a positive integer (or 0 to stop): "))



    









