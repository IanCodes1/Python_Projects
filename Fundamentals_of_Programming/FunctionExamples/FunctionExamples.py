# File: FunctionExamples.py

# Description of Program: Program contains a library of functions that can be imported to do various mathematical calulations.

import math

# 1. Write a function to return the sum of three numbers.

def sum3Numbers (x, y, z):
    return x + y + z


# 2. Write a function to multiply three numbers.

def multiply3Numbers( x, y, z ):
    return x * y * z


# 3. Write a function to return the sum of up to 3 numbers.  It should
#    accept 1, 2, or 3 parameters.  Hint: any parameter not given
#    should default to 0.

def sumUpTo3Numbers (x, y = 0, z = 0):
    return x + y + z

   
# 4. Write a function to return the product of up to 3 numbers.  It
#    should accept 1, 2, or 3 parameters.  Hint: what should the
#    default be in this case?

def multiplyUpTo3Numbers (x, y = 1, z = 1):
    return x * y * z


# 5. Write a function that takes 2 numbers as input and prints them
#    out in ascending order.

def printInOrder( x, y ):
    if x > y:
        x,y = y,x
    else:
        x,y = x,y
    print(x,y)

# 6. Write a function that returns the area of a square, given the length of a side.
#    Print an error message if side is negative. 

def areaOfSquare( side ):
    if side >= 0:
        return side ** 2
    else:
        return "Negative value entered"


# 7. Write a function that returns the perimeter of a square, given
#    the length of a side.  Print an error message if side is negative.

def perimeterOfSquare( side ):
    if side >= 0:
        return side * 4
    else:
        return "Negative value entered"


# 8. Write a function that returns the area of a circle, given the
#    radius.  Use math.pi. Print an error message if radius is negative.

def areaOfCircle( radius ):
    if radius >= 0:
        return math.pi * radius ** 2
    else:
        return "Negative value entered"


# 9. Write a function that returns the circumference of a circle given
#    the radius.  Use math.pi. Print an error if radius is negative.

def circumferenceOfCircle( radius ):
    if radius >= 0:
        return 2 * math.pi * radius
    else:
        return "Negative value entered"


# 10. Write a function: given parameters d1, d2, x, returns whether
#    both d1 and d2 are both factors (evenly divide) x.  You can
#    assume all values are integers.

def bothFactors( d1, d2, x ):
    if x % d1 == 0 and x % d2 == 0:
        return True
    else:
        return False


# 11. Given a value x, compute and print out the area and circumference of a circle with
#    radius x and the area and perimeter of a square with side x.  Use your previous 
#    functions for these computations.  Leave a blank line above and below the printing.

def squareAndCircle( x ):
    print()
    print("Circle with radius",x,"has:")
    print("   Area:",areaOfCircle(x))
    print("   Circumference: ",circumferenceOfCircle(x))
    print("Square with side",x,"has:")
    print("   Area:",areaOfSquare(x))
    print("   Perimeter:",perimeterOfSquare(x))
    print()



# 12. Write a function that returns the factorial of a positive
#     integer n.  Use a for loop to compute the factorial.  You can
#     assume the input is an integer, but print an error message if
#     it's not positive and return None.

def factorial( n ):
    if n < 1:
        return "Input must be positive."
    result = 1    
    for i in range(1,n+1):
        result = result * i 
        
    return result
