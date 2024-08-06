# While-Loop


"""
var = int( input("Enter an integer divisble by 3: "))

while var%3 != 0:
    var = int(input("Enter an integer divisble by 3: "))
else:
    print("%d is an integer divisible by 3"%var)

print()

# For-Loop
x = [1, 10, 34, 12, 21, 19]

for i in x: 
    if i > 2:
        continue
    print(i)    

print() 

x = (input("Enter the number of rows: "))
y = 2 * x - 1
n = y
while n >= 1 :
    space = y - n // 2
    for j in range(1, space + 1):
        print(" ",end="")
    for i in range(1, n+1):
        print("*",end="")
    for k in range(1, space + 1):
        print(" ",end="")
    print()
    n = n-2


# Program counts the number of positive and negative integers entered by user   
x = int( input(""))
countNeg = 0
countPos = 0

while x > 0:
    x = int(input(""))
    countPos = countPos+1
    while x < 0:
      x = int(input(""))
      countNeg = countNeg+1
    
print(countPos,countNeg)



t = 10000
y = int( input(" "))

while y >= 0 :
    y = int(input(" "))
    print(t + (t * 0.05))

# Add dollar sign
print(y, ",.2f")
"""
posInt = int( input(" ")) #positive integer user input
count = 0
if posInt == 0:
    print(1)
    while posInt % 2 == 0:
        count = count+1
    else:
        print(sum(posInt))
    

