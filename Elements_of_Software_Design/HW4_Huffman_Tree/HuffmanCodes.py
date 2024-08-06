#  File: HuffmanCodes.py
#  Student Name: Ian Salinas
#  Student UT EID: ibs325
# Python Huffman Compression
from PriorityQueue import PriorityQueue
import sys


# Huffman Node Class
class Huffman_Node(object):
    def __init__(self, ch=None, count=0, left=None, right=None):
        self.ch = ch
        self.count = count
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.count < other.count

    def __str__(self):
        if self.ch is None:
            ch = "*"
        else:
            ch = self.ch
        return ch + ", " + str(self.count)


# Build Character Frequency Table
# uses dictionary
# characters added in the order they first occur
def build_char_freq_table(inputString):

    # ADD CODE HERE
    table = {}

    for currentChar in inputString:         # Iterates through input string 
        if currentChar not in table:        # Checks if character is not in the table dictionary
            table[currentChar] = 1          
        else:
            table[currentChar] += 1         # If it is in the table it will move on to next iteration

    return table


# Builds the Huffman Tree
# Creates Huffman Nodes, some pointing to others.
# Returns the root node
def build_huffman_tree(inputString):
    # Build the frequency table, a dictionary of character, frequency pairs
    freq_table = build_char_freq_table(inputString)

    # Build a priority queue, a queue of frequency, character pairs
    # Hightest priority is lowest frequency
    # When a tie in frequency, first item added will be removed first
    priorities = PriorityQueue()
    for key in freq_table:
        node = Huffman_Node(ch=key, count=freq_table[key])
        priorities.push(node)

    # Builds internal nodes of huffman tree, connects all nodes
    while (priorities.get_size() > 1):

        # ADD CODE HERE
        left = priorities.pop()     # First pop = left node
        right = priorities.pop()    # Second pop = right node

        count = left.count + right.count        # Sum of the counts of children nodes

        combined_nodes = Huffman_Node(ch = None, count = count, left = left, right = right)         # Creates new Huffman_Node object that utilizes the combined left and right nodes
        
        priorities.push(combined_nodes)         # Push works like "append" in that it is pushing the item into the priority "queue"

    # At the end, priority queue is empty
    # Return the root node of the Huffman Tree
    return priorities.pop()


# After Huffman Tree is built, create dictionary of
# characters and code pairs
def get_huffman_codes(node, prefix, codes):
    if (node.left is None and node.right is None):
        codes[node.ch] = prefix
    else:
        get_huffman_codes(node.left, prefix + "0", codes)
        get_huffman_codes(node.right, prefix + "1", codes)
    return codes


# For each character in input file, returns the Huffman Code
# Input file uses <space> to indicate a space
# If character not found, display "No code found"
def process_chars(data, huff_codes):

    # ADD CODE HERE
    print(f"{'Character':<13}{'Code'}")                 # Formats strings to given output

    result = {}     # Dictionary to store chars and huffman codes

    for line in data[1:]:                   # Loops over lines in data list, skipping first element utilizing slicing
        chars = line.strip()
        if chars[0] == "<":
            chars = " "
        elif len(chars) > 1:                 # Checks if stripped line has more than one char
            chars = chars[0]

        if chars in huff_codes:
            code = huff_codes[chars]         # Gets huffman code if it exists
        else:
            code = "No code found"
            
        result[chars] = code                 # Adds char and huffman code to the "results" dictionary
        print(f'{chars:<13}{code}')         

    return result

    ''' DRIVER CODE '''

# Open input source
# Change debug to false before submitting
debug = False
if debug:
    in_data = open('message.in')
else:
    in_data = sys.stdin

# read message
data = in_data.readlines()
message = data[0].strip()

# Build Huffman Tree and Codes
root = build_huffman_tree(message)
huff_codes = get_huffman_codes(root, "", {})

# display code for each character in input file
process_chars(data, huff_codes)



