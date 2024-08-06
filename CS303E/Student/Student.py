# File: Initials.py
# Student: Ian Salinas
# UT EID: ibs325
# Course: CS303E
# 
# Date: 10/11/22
# Description of Program: Program allows user to enter in the name of a student and their two exam grades. When called upon, the user can find each individual piece of the program by calling it. 

class Student:

    def __init__(self, name, ex1 = None, ex2 = None):


        self.__name = name
        self.__ex1 = ex1
        self.__ex2 = ex2


    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.name = name


    def getExam1(self):
        return self.__ex1

    def getExam2(self):
        return self.__ex2


    def setExam1(self, ex1):
        self.__ex1 = ex1

    def setExam2(self,ex2):
        self.__ex2 = ex2


    def getAverage(self):
        if self.__ex1 == None or self.__ex2 == None:
            avg = print("Some exam grades not available.")
        else:
            avg = (self.__ex1 + self.__ex2) / 2
            return print(avg)

    def __str__(self):
        return "Student: " + str(self.__name) +  "\n  Exam1: " + str(self.__ex1) + "\n  Exam2: " + str(self.__ex2)