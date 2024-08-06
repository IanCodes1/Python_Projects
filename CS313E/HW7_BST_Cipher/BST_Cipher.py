#  File: BST_Cipher.py
#  Student Name: Ian Salinas
#  Student UT EID: ibs325
#  Partner Name: Nicholas Gonzalez
#  Partner UT EID: ng25878

import sys

# One node in the BST Cipher Tree


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None


# The BST Cipher Tree
class Tree:

    # Create the BST Cipher tree based on the key
    def __init__(self, key):
        # This is for debug purposes only.
        # Comment out or delete before submitting.
        # key_tree.BST_print()
        '''##### ADD CODE HERE #####'''

        self.root = None
        key = self.clean(key)

        for ch in key:
            if self.root is None:
                self.root = Node(ch)
            else:
                self.insert(ch)

    # Insert one new charater/Node to the BST Cipher tree
    # If the character already exists, don't add it.
    def insert(self, ch):
        '''##### ADD CODE HERE #####'''

        if self.root is None:
            self.root = Node(ch)
            return
        
        current = self.root

        while True:
            if ch == current.ch:        # checks for duplicate characters and does not insert if duplicate
                return
            if ch < current.ch:     # if char is smaller than current... move left
                if current.left is None:
                    current.left = Node(ch)
                    return
                else:
                    current = current.left
            else:
                if current.right is None:        # if char is larger than current... move right
                    current.right = Node(ch)
                    return
                else:
                    current = current.right

    # Encrypts a text message using the BST Tree
    def encrypt(self, message):
        '''##### ADD CODE HERE #####'''

        encrypted_msg = ''
        clean_msg = self.clean(message)

        for ch in clean_msg:        # iterate through each char in the clean message
            encrypted_msg += self.encrypt_ch(ch) + "!"      # adds the encrypted character to the empty encrypted variable
        return encrypted_msg[:-1]       # this returns the encrypted message and removes the last exclamation point
    


            
    # Encrypts a single character
    def encrypt_ch(self, ch):
        '''##### ADD CODE HERE #####'''

        encrypted_msg = ''
        node = self.root

        while node is not None:     # Loop until the node is None
            if ch == node.ch:       # Checks if current character is = to the character of the node
                if ch == self.root.ch:
                    encrypted_msg = '*' + encrypted_msg
                return encrypted_msg #+ '*'
            
            elif ch < node.ch:      # if char is smaller than node char... move down to the left
                encrypted_msg += '<'
                node = node.left

            else:
                encrypted_msg += '>'    # if char is bigger than the node char... move down to the right
                node = node.right

        return encrypted_msg
    
    # Decrypts an encrypted message using the BST Tree
    def decrypt(self, codes_string):
        '''##### ADD CODE HERE #####'''

        codes = codes_string.split('!')     # splits the code by every ! it reads
        decrypted = ''

        for ch in codes:        # iterates through the code
            decrypted += self.decrypt_code(ch)      # adds decrypted code to the decrypted string
        return decrypted
    
    # Decrypts a single code
    def decrypt_code(self, code):
        '''##### ADD CODE HERE #####'''

        current = self.root    

        for ch in code:         # iterates through each character in "code"
            if current is None:
                return ''
            
            if ch == '>':               # Navigates left or right based on the char
                current = current.right

            elif ch == '<':
                current = current.left

        if current:         # returns the char of "current" node or '' if current is None
            return current.ch
        else:
            return ''

    # Get printed version of BST for debugging
    def BST_print(self):
        if self.root is None:
            return "Empty tree"
        self.BST_print_helper(self.root)

    # Prints a BST subtree
    def BST_print_helper(self, node, level=0):
        if node is not None:
            if node.right is not None:
                self.BST_print_helper(node.right, level + 1)
            print('     ' * level + '->', node.ch)
            if node.left is not None:
                self.BST_print_helper(node.left, level + 1)

    def clean(self, text):
        cleanText = ""
        for i in range(len(text)):
            if (self.isValidCh(text[i])):
                cleanText += text[i]
        return cleanText

    # Utility method
    def isValidLetter(self, ch):
        if (ch >= "a" and ch <= "z"):
            return True
        return False

    # Utility method
    def isValidCh(self, ch):
        if (ch == " " or self.isValidLetter(ch)):
            return True
        return False


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)

    # read string to be encrypted
    text_message = in_data.readline().strip()

    # print the encryption
    print(key_tree.encrypt(text_message))

    # read the string to be decrypted
    coded_message = in_data.readline().strip()

    # print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()
