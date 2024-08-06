#  File: ExpressionTree.py
#  Student Name: Ian Salinas
#  Student UT EID: ibs325
#  Partner Name: Nicholas Gonzalez
#  Partner UT EID: ng25878

import sys

# list of valid operators
operators = ['+', '-', '*', '/', '//', '%', '**']


# Input: Elements of a simple expression
#        operator (String) and two operands (numbers)
# Output: result of evaluation of the expression
def operation(operator, n, m):
    expression = str(n) + operator + str(m)
    return eval(expression)


# Stack Class - DO NOT CHANGE
# Traditional Stack implementation containing list of data items
# Used to keep track of items in nested expressions.
class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


# Node Class
# Purpose: Used by the Tree Class to represent one operand or operators
#          in a binary expression. It includes data (a character) and
#          two pointers, to the left and right child nodes.
# You do not need to make changes to this class.
class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


# Tree Class
# Purpose: To represent the string representation of operators and operands
#          of a binary expression so it can be evaluated.
# You need to make a lot of changes to this class!
class Tree (object):
    def __init__(self):
        self.root = Node(None)

    # Input: a string expression
    # Output: an expression tree
    def create_tree(self, expr):
        '''##### ADD CODE HERE #####'''
        stack = Stack()
        self.root = Node(None)
        current = self.root

        for char in expr.split():           # Iterates through the expression and allows us to validate and check each character
            
            if char == "(":                 # if character is a "(" then lets check the data
                if current.data is None:    # if current node is empty... this is a root node and push this root node into the stack 
                    stack.push(current)
                    current.lChild = Node(None)     
                    current = current.lChild    # update current to left child of the root node
                else:
                    current.rChild = Node(None) # if data exists in the node already...create a right child node... update current to right child of the previous node
                    stack.push(current)
                    current = current.rChild
            
            elif char in operators:     # if character is one of the operators in the list of operators given...
                current.data = char     # Insert character into the current node
                current.rChild = Node() # Create right child node
                stack.push(current)     # Add root node to stack so we can get back to it
                current = current.rChild    # Update current to right child 

            elif char in operators:     # if a character is an operator...

                current.data = char         # set current node's data to the operator
                prev_current = current      # Prep right child for next node

                current.rChild = Node(None)
                current = current.rChild
                stack.push(prev_current)    # Pushes operator node to the stack

            elif char == ")":               # Marks the end of an expression
                if not stack.is_empty():
                    current = stack.pop()
            
            else:                       # Check if number in expression is a float or integer
                if '.' in char:
                    current.data = float(char)
                else:
                    current.data = int(char)
                
                if not stack.is_empty():
                    current = stack.pop()
                
        if self.root.data is None:      # Handles case if root node is a temp node with no data and has a child
            if self.root.lChild is not None:
                self.root = self.root.lChild    # Simply updates the empty root node to the left child

            elif self.root.rChild is not None:
                self.root = self.root.rChild    # Simply updates the empty root node to the right child


    # Input: A node in an expression tree
    # Output: The result of evaluating the expression
    #         with this node as the root
    def evaluate(self, current):
        '''##### ADD CODE HERE #####'''
        if current == None:
            return None
        
        if current.data == None:
            return None

        if current.data in operators:
            left_child = self.evaluate(current.lChild)
            right_child = self.evaluate(current.rChild)

            return operation(current.data, left_child, right_child)
        
        else:
            return float(current.data)

    # Starter Method for pre_order
    # Input: a node in an expression tree
    # Output: (string) the preorder notation of the expression
    #                  with this node a the root
    def pre_order(self, current):
        '''##### ADD CODE HERE #####'''
        if current == None:
            return ""
        
        else:
            return (str(current.data) + ' ' + self.pre_order(current.lChild) + '' + self.pre_order(current.rChild))
        

    # Starter Method for post_order
    # Input: a node in an expression tree
    # Output: (string) the post order notation of the expression
    #                  with this node a the root
    def post_order(self, current):
        '''##### ADD CODE HERE #####'''
        if current == None:
            return ""
        
        else:
            return self.post_order(current.lChild) + '' + self.post_order(current.rChild) + ' ' + str(current.data)

''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('expression.in')
    else:
        in_data = sys.stdin

    # read infix expression
    line = in_data.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
