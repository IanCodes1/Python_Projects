# File: Initials.py

# Description of Program: Program uses multiple functions to divide the computations of assignments to find their averages. Program then uses these functions to calulate a students average and letter grade in a class. 




# Computes the average of three homework assignment grades given by the user
def computeHomeworkAvg():
    print()
    print("HOMEWORKS:")

    while True:
        hw1 = int(input("  Enter HW1 grade: "))
        if hw1 < 0 or hw1 > 10: 
            print("  Grade must be in range [0..10]. Try again.")
        else:
            break
    while True:
        hw2 = int(input("  Enter HW2 grade: "))
        if hw2 < 0 or hw2 > 10: 
            print("  Grade must be in range [0..10]. Try again.")
        else:
            break
    while True:
        hw3 = int(input("  Enter HW3 grade: "))
        if hw3 < 0 or hw3 > 10: 
            print("  Grade must be in range [0..10]. Try again.")
        else:
            break

    hwAvg = ((hw1 + hw2 + hw3) / 3) * 10
    return hwAvg




# Computes the average of two project grades given by the user 
def computeProjectAvg():
    print()
    print("PROJECTS:")

    while True:
        pr1 = int(input("  Enter Pr1 grade: "))
        if pr1 < 0 or pr1 > 100:
            print("  Grade must be in range [0..100]. Try again.")
        else:
            break
    while True:
        pr2 = int(input("  Enter Pr2 grade: "))
        if pr2 < 0 or pr2 > 100:
            print("  Grade must be in range [0..100]. Try again.")
        else:
            break
    pAvg = (pr1 + pr2) / 2
    return pAvg



# Computes the average of two exams given by the user
def computeExamAvg():

    print()
    print("EXAMS:")

    while True:
        ex1 = int(input("  Enter Ex1 grade: "))
        if ex1 < 0 or ex1 > 100:
            print("  Grade must be in range [0..100]. Try again.")
        else:
            break

    while True:
        ex2 = int(input("  Enter Ex2 grade: "))
        if ex2 < 0 or ex2 > 100:
            print("  Grade must be in range [0..100]. Try again.")
        else:
            break
    
    eAvg = (ex1 + ex2) / 2
    return eAvg
   

# Computes the course average using the average values found from the homework, project, and exam functions
def computeCourseAvg(x, y, z):

    return (x * 0.30) + (y * 0.30) + (z * 0.40)
    
def avgToLetterGrade(x):

    if x >= 90 and x <= 100:
        return "A"
    elif x >= 80 and x < 90:
        return "B"
    elif x >= 70 and x < 80:
        return "C"
    elif x >= 60 and x < 70:
        return "D"
    elif x >= 0 and x < 60:
        return "F"



# Compiles the student's averages and prints the letter grade
def computeStudentGradeReport():

    hwAvg = computeHomeworkAvg()
    pAvg = computeProjectAvg()
    eAvg = computeExamAvg()

    Avg = computeCourseAvg(hwAvg, pAvg, eAvg)
    let = avgToLetterGrade(Avg)
    
    print()
    print("Grade report for:",name,"")
    print("  Homework average (30% of grade):", format(hwAvg, "0.2f"))
    print("  Project average (30% of grade):", format(pAvg, "0.2f"))
    print("  Exam average (40% of grade):", format(eAvg, "0.2f"))
    print("  Student course average:", format(Avg, "0.2f"))
    print("  Course grade (CS303E: Fall, 2022):", let)
    print()



while True:
    name = input("Enter the student's name (or 'stop'): ")
    if name == 'stop':
        print("Thanks for using the grade calculator! Goodbye.")
        print()
        break
    else:
        computeStudentGradeReport()





 




    





    
