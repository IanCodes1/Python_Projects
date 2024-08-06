# File: MinMax.py

# Description of Program: Program utilizes and compares linear and binary search programs in order to find how closely their averages match numerical outputs. 

import random
import math

def linearSearch( lst, key ):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """
    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)

# Linear search 
x = 0
Rlist = [x for x in range(0,1000)] # Creates random list
random.shuffle(Rlist) # Shuffles random list
probe = 0

print("Linear search: ")

def linearTest(nValue):
    numCompare = 0
    for i in range(nValue):
        key = random.randrange(0,1000)
        probe = linearSearch(Rlist, key) + 1
        numCompare += probe
    avgProbe = numCompare / i
    return avgProbe

print("  Tests: 10       Average probes:",linearTest(10))
print("  Tests: 100      Average probes:",linearTest(100))
print("  Tests: 1000     Average probes:",linearTest(1000))
print("  Tests: 10000    Average probes:",linearTest(10000))
print("  Tests: 100000   Average probes:",linearTest(100000))


# Binary search
Blist = [x for x in range(0,1000)]

print("Binary search:")

def binaryTest():
    numCompare = 0
    for i in range(1000):
        key = random.randrange(0,1000)
        index, probe = binarySearch(Blist,key)
        numCompare += probe
    avgProbe = numCompare / 1000
    return avgProbe

result = binaryTest()


print("  Average number of probes:", result)
print("  log2(1000):", math.log2(1000))
difference = math.log2(1000) - result
print("  Differs from log2(1000) by :", difference)


    
