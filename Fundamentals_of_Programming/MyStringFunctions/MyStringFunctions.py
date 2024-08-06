# File: Initials.py
# Student: Ian Salinas
# UT EID: ibs325
# Course: CS303E
# 
# Date: 10/17/22
# Description of Program: Program practices how to manipulate strings within class functions. 



def myAppend( s , ch ):
        return s + ch

def myCount( s, ch ):
    # Return the number of times character ch appears
    # in s.
    count = 0 
    for c in s:
        if c == ch:
            count += 1
    return count


def myExtend( s1, s2 ):
    # Return a new string that contains the elements of
    # s1 followed by the elements of s2, in the same
    # order they appear in s2.

    return s1 + s2

def myMin( s ):
    # Return the character in s with the lowest ASCII code.
    # If s is empty, print "Empty string: no min value"
    # and return None.
    
    if s == "" :
        print("Empty string: no min value")
        return None
    else:
        return min(s)

def myInsert( s, i, ch ):
    # Return a new string like s except that ch has been
    # inserted at the ith position. I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of s and return None.


# split the first string 

    if i > len(s):
        print("Invalid index")
        return None
    
    return s[:i] + ch + s[i:]
        
       
def myPop( s, i ):
    # Return two results: 
    # 1. a new string that is like s but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(s), and return s unchanged and None
       
    if i >= len(s):
        print("Invalid index")
        return None
    
    return s[:i] + s[i+1:], s[i] 



def myFind( s, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.

    for i in range(len(s)):
        if s[i] == ch:
            return i
    return -1


def myRFind( s, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
            
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ch:
            return i
        if ch not in s:
            return -1


def myRemove( s, ch ):
    # Return a new string with the first occurrence of ch 
    # removed. If there is none, return s.

    for i in range(len(s)):
        if s[i] == ch:
            return s[:i] + s[i+1:]
    return s
    

def myRemoveAll( s, ch ):
    # Return a new string with all occurrences of ch.
    # removed. If there are none, return s.

    string = ""
    for i in range(len(s)):
        if s[i] != ch:
            string += s[i]
    return string


def myReverse( s ):
    # Return a new string like s but with the characters
    # in the reverse order.

    return s[::-1]

