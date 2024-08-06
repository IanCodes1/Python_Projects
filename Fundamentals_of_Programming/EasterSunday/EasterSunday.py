# File: EasterSunday.py
# Student: Ian Salinas
# UT EID: ibs325
# Course Name: CS303E
#
# Date: 09/03/2022
# Description of Program: Program uses a variety of mathematical calulations and variables to produce the date of Easter for any given year.

y = int( input("Enter year: ") )
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32

# Statement uses calculations from above
print("In", y ,"Easter Sunday is on month", n ,"and day", p)



