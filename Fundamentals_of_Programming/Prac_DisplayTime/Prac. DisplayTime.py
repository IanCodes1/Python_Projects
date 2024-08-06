
"""
# Prompt the user for input
seconds = int(input("Enter an integer for seconds: ")) # int or eval works

# Get minutes and remaining seconds 
minutes = seconds // 60 # Find minutes in seconds
remainingSeconds = seconds % 60 #Seconds remaining

print(seconds, "seconds is", minutes,
    "minutes and ", remainingSeconds, "seconds")

seconds = int(input("Enter an integer for seconds: ")) # int or eval works



minutes = seconds // 60 
remainingSeconds = seconds % 60 

print(seconds, "seconds is", minutes, "minutes and", remainingSeconds, "seconds" )


# int is for whole number integers (Ex: 0, 1, 2, 3)
# float is for decimal or fractional number (Ex: 0.123, 1.234, 2.345)
# eval will take any string inputted into the system, an integer or a fractional number


print(42 / 5)
print( 42 //5)
print(42 % 5)
print(1 % 2)
print(2 % 1)
print(45 + 4 * 4 - 2)
print( 45 + 43 % 5 * (23 * 3 % 2))
print(5 ** 2)
print(5.1 ** 2)


#Program calulates the day of the week when user enters the starting day and x amount of days from the original start date. 

today = int(input("Enter number of the day of the week (Monday = 1 and Sunday = 7): "))
hypo = int(input("Enter hypothetical days from start date: "))
result = hypo % 7 
final = today + result


print("In", hypo,"days, the day of the week will be", final,".")



# Rewrite to become an integer
print(25 / 4) 
print(25 // 4)

"""
a = 1
b = 2
c = 3
d = 4
r = 5


print(4 / 3 * (r + 34) - 9 * (a + b * c) + 3 + d * (2 + a ) / a + b * d)
