# File: Project3.py

# Description of Program: Program creates ciphered text and is able to encrypt and decrypt files the user enters.

import random
import os

LETTERS = "abcdefghijklmnopqrstuvwxyz"


def isLegalKey(key):
    key = key.lower()   # converts key to lowercase
    return (len(key) == 26 and all( [ch in key for ch in LETTERS])) # returns a 26-digit key that are in the variable LETTERS
    
def makeRandomKey():
    list1 = list(LETTERS)
    random.shuffle(list1)
    return ''.join(list1)   # shuffles LETTERS variable and creates a random key

def makeConversionDictionary(key1, key2):
    pass
    dict = {}
    for i in range(26):
        dict[key1[i]] = key2[i] # adds the converted key to a dictionary
    return dict

def convertCharacter(ch,d):
    if ch.isalpha() == False:
        return ch
    elif ch.isupper():
        ch = ch.lower()
        ch = d[ch]  # d = dictionary
        ch = ch.upper()
        return ch
    else:
        return d[ch]    # returns converted character

def convertText (text,d):
    nString = ""

    for ch in text:
        nChar = convertCharacter(ch,d)
        nString = nString + nChar   # adds new converted characters to a new string (nString)
    return nString  


class SubstitutionCipher:
    def __init__(self,key = makeRandomKey()):
        self.__key = key

    def getKey(self):
        return self.__key
        
    def setKey(self, newKey):
        self.__key = newKey

    def encryptFile(self, inFile, outFile):
        if os.path.isfile(inFile):
            inputFile = open(inFile, "r")   # reads the file inputed by user
            outputFile = open(outFile, "w") # re-writes the inputed file from the user
            dictionary = makeConversionDictionary(LETTERS, self.__key) # converts the given key into an encrypted key

            line = inputFile.readline() # reads a line of text
            while line: # while the line is not empty
                convertLine = convertText(line,dictionary)  # converts the characters on the line it is reading and adds it to a dictionary
                outputFile.write(convertLine)   # writes the string stored in the dictionary
                line = inputFile.readline()     # reads the next line
            inputFile.close()
            outputFile.close()  # closes both the inputed file and the new encrypted file created
            print("The encrypted output filename is", outFile)
        else:
            print("File does not exist")
        print()



    def decryptFile (self, inFile, outFile):
        if os.path.isfile(inFile):
            inputFile = open(inFile, "r")
            outputFile = open(outFile, "w")
            dictionary = makeConversionDictionary(self.__key, LETTERS) # converts the given encrypted key back to the original text

            line = inputFile.readline()
            while line:
                convertLine = convertText(line,dictionary)
                outputFile.write(convertLine)
                line = inputFile.readline()
            inputFile.close()
            outputFile.close()
            print("The decrypted output filename is", outFile)
        else:
            print("File does not exist")
        print()

def main():
    enc = SubstitutionCipher()

    while True:
        command = str(input("Enter a command (getKey, changeKey, encryptFile, decryptFile, quit): ")).lower()

        if command == "getkey":
            print("  Current cipher key:", enc.getKey())
            print()
            continue
        elif command == "changekey":
            while True:
                newkey = str(input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")).lower()

                if newkey == "quit":
                    print()
                    break
                elif newkey == "random":
                    newkey = makeRandomKey()
                    enc.setKey(newkey)
                    print("   New cipher key:", newkey)
                    print()
                    break
                elif isLegalKey(newkey):
                    enc.setKey(newkey)
                    print("   New cipher key:", newkey)
                    print()
                    break
                else:
                    print("    Illegal key entered. Try again!")

        elif command == "encryptfile":
            fileName = input("  Enter a filename: ")
            extension = "-Enc"
            if fileName.endswith(".txt"):
                outFile = fileName[:-4] + extension + ".txt"
            else:
                outFile = fileName + extension
            enc.encryptFile(fileName, outFile)


        elif command == "decryptfile":
            fileName = input("  Enter a filename: ")
            extension = "-Dec"
            if fileName.endswith(".txt"):
                outFile = fileName[:-4] + extension + ".txt"
            else:
                outFile = fileName + extension
            enc.decryptFile(fileName, outFile)


        elif command == "quit":
            print("Thanks for visiting!\n")
            return
        else:
            print("  Command not recognized. Try again!\n")


main()

