# Quiz Game Project (Version 2)
# Ian Salinas

import random
import numpy as np

with open("/Users/ian/Library/CloudStorage/OneDrive-TheUniversityofTexasatAustin/Python Projects/External Files/correct_responses.csv", "r") as file:
    c_ans_list = file.readlines()
    c_ans_list = [line.strip() for line in c_ans_list]

with open("/Users/ian/Library/CloudStorage/OneDrive-TheUniversityofTexasatAustin/Python Projects/External Files/incorrect_responses.csv", "r") as file:
    w_ans_list = file.readlines()
    w_ans_list = [line.strip() for line in w_ans_list]

np_c_list = np.array(c_ans_list)
np_w_list = np.array(w_ans_list)

# Welcomes User
print()
print('Welcome to my quiz game!')
print()

playing = input('Would you like to play? ')

# Checks for yes answers to proceed
while playing.lower() == 'yes':
    print()
    print("Okay! Let's play :)")
    print()
    break
else:
    print("Okay! See you next time :)")
    print()
    quit()

score = 0

# Q1

while True:
    answer = input("What does CPU stand for? ")

    if answer.lower() == "central processing unit":
        print(random.choice(np_c_list))
        print()
        score += 1
        break
    else:
        print(random.choice(np_w_list))
        print()
        score -= 1

print()

# Q2

while True:
    answer = input("What does GPU stand for? ")

    if answer.lower() == "graphics processing unit":
        print(random.choice(np_c_list))
        print()
        score += 1
        break
    else:
        print(random.choice(np_w_list))
        print()
        score -= 1

print()
# Q3
while True:
    answer = input("What does RAM stand for? ")

    if answer.lower() == "random access memory":
        print(random.choice(np_c_list))
        print()
        score += 1
        break
    else:
        print(random.choice(np_w_list))
        print()
        score -= 1

print()
# Q4
while True:
    answer = input("What does PSU stand for? ")

    if answer.lower() == "power supply unit":
        print(random.choice(np_c_list))
        print()
        score += 1
        break
    else:
        print(random.choice(np_w_list))
        print()
        score -= 1

print()
print("You got " + str(score) +
      " questions correct! Your percentage score is " + str(str(score/4 * 100) + "%"))

print()
print()
print("Thank you for playing! See you soon!")
print()
print()
