# File: WordleAssistant.py
# Student: Ian Salinas
# UT EID: ibs325
# Course: CS303E
# 
# Date: 11/05/2022
# Description of Program: Program uses various functions to provide the user with a new list of words filtered with parameters set by the user.

# https://www.cs.utexas.edu/~byoung/cs303e/hw11.html (temp. link to hw b/c website is down)

def createWordlist(filename): 
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'. Return
    the list of words and the number of words as a pair. """

    word = open(filename, "r")
    newList = []
    listt = word.readlines()

    for w in listt:
        firstLet = w.strip()
        if len(firstLet) == 5 and firstLet[len(firstLet)- 1] != 's' \
        and len(firstLet) == len(set(firstLet)):
            newList.append(firstLet)

    return newList, len(newList)
    

def containsAll(wordlist, include):
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include. 
    """
    endResult = set()
    nInclude = set(include)

    for w in wordlist:
        count = 0
        for c in nInclude:
            if c in w:
                count += 1
        if count == len(nInclude):
            endResult.add(w)
    return endResult

def containsNone(wordlist, exclude):
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude. 
    """
    endResult = set()
    nExclude = set(exclude)

    for w in wordlist:
        count = 0
        for c in nExclude:
            if c not in w:
                count += 1
        if count == len(nExclude):
            endResult.add(w)
    return endResult

def containsAtPositions(wordlist, posInfo):
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4]. Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.  This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """

    result = set()
    
    for word in wordlist:
        valid = True
        for let in posInfo:
            if word[posInfo[let]] != let:
                valid = False
                break
        if valid == True:
            result.add(word)        
    return result


def getPossibleWords(wordlist, posInfo, include, exclude):
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from 
    the wordlist that contains the words that satisfy all of 
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude.
    """
    result1 = containsAtPositions(wordlist,posInfo)
    result2 = containsAll(result1, include)
    result3 = containsNone(result2, exclude)

    return result3

"""
def main():

    wordlist, count = createWordlist('wordlist.txt')
    print(count)
    print()

    setABC = containsAll(wordlist,'abc')
    print(setABC)
    print()

    setXYZ = containsAll( wordlist, 'xyz' )
    print(setXYZ)
    print()

    someWords = containsNone(wordlist,'abcdefghijklmn')
    print(someWords)
    print()

    someMoreWords = containsNone( wordlist, 'abcdefghijklmnopqrstuvw' )
    print(someMoreWords)
    print()

    posInfo = {'a':0, 'y':4}
    print(containsAtPositions(wordlist, posInfo))
    print()

    PossibleWords = getPossibleWords(wordlist, {'a':0,'b':1},"o","v")
    print(PossibleWords)
"""