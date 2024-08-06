# File: MinMax.py
# Student: Ian Salinas
# UT EID: ibs325
# Course: CS303E
# 
# Date: 09/23/2022
# Description of Program: Program asks user to enter integers for it to calculate the maximums and minimums out of the numbers given. Program is also stopped when user enter 'stop'.

print()
# Sets variables
inp = input("Enter an integer or 'stop' to end: ")
min = inp
max = inp
COUNT = 0
i = COUNT

# While Loop which prompts the user to enter integers or 'stop' to end the string
while True:
    inp = input("Enter an integer or 'stop' to end: ")
    if (inp == "stop"):
        break
    if min is inp or min > inp: #Calculates the integer with the minimum value of the set
        min = inp
    if max is inp or max < inp: #Calculates the integer with the maximum value of the set
        max = inp
    
print()
#Calulates how many times the loop is run and prints out the counter
while i <= 0:
    print("You entered",i,"numbers")
    break
# Maximum and minimum value of the integer set given by the user     
print("The maximum is", max ,"")
print("The minimum is", min ,"")
print()
        




    

        






