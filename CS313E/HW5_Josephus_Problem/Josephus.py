#  File: Josephus.py
#  Student Name: Ian Salinas
#  Student UT EID: ibs325
#  Partner Name: Nicholas Gonzalez
#  Partner UT EID: ng25878

import sys


# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None

    # Is the list empty
    def is_empty(self):
        return self.first is None

    # Append an item at the end of the list
    def insert(self, data):
        pass
        '''##### ADD CODE HERE #####'''
        new_soldier = Link(data)

        if self.is_empty():             # If empty set new soldier to head node and tail node
            self.first = new_soldier
            self.last = new_soldier
            new_soldier.next = new_soldier
        else:
            new_soldier.next = self.first       # If not empty append new soldier
            self.last.next = new_soldier
            self.last = new_soldier


    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        if self.is_empty():
            return None
        
        current = self.first
        while not False:
            if current.data == data:
                return current      # Soldier found and returns soldiers location/node
            current = current.next

            if current == self.first:
                break

        return None    # No soldier found
        
        '''##### ADD CODE HERE #####'''

    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data):

        if self.is_empty():
            return None
    
        current = self.first
        prev = self.last

        while True:
            if current.data == data:
                if current == self.first:
                    if self.first == self.last:  # Checks if there is only one node
                        self.first = None
                        self.last = None
                    else:
                        self.first = self.first.next
                        self.last.next = self.first
                elif current == self.last:      # Checks if this is the last soldier
                    self.last = prev
                    self.last.next = self.first
                else:   
                    prev.next = current.next       # Deletes middle node
            
                return current  # Returns the killed soldier... (deleted node lol)

            prev = current
            current = current.next
        
            if current == self.first:  # If everyone is dead... return none
                return None

    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step):
        
        '''##### ADD CODE HERE #####'''
        if self.is_empty():
            return None,None
        
        current = self.find(start)      # Looks for new starting node after killing the last
        
        if current is None:
            return None,None
        
        for i in range(step - 1):
            current = current.next
        self.delete(current.data)

        return current.data,current.next

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        
        '''##### ADD CODE HERE #####'''
        if self.is_empty():
            return "[]"
        
        soldier_list = []
        current = self.first

        while True:
            soldier_list.append(str(current.data))
            current = current.next
            
            if current == self.first:
                break
        return "[" + ", ".join(soldier_list) + "]"

# Input: Number of soldiers
# Outupt: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):
    
    '''##### ADD CODE HERE #####'''
    circular_list = CircularList()

    for soldier in range(1, num_soldiers + 1):
        circular_list.insert(soldier)

    return circular_list


# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):
    
    '''##### ADD CODE HERE #####'''
    current = my_list.find(start_data)

    if not current:
        return None
    
    while num_soldiers > 1:
        for i in range(step_count - 1):
            current = current.next    
        print(current.data)     # Print data of current soldier to be eliminated

        next_node = current.next    # Saves next soldier before deleting current... this is bc it will be our new start
        
        my_list.delete(current.data)    # MURDERS CURRENT SOLDIER... or deleted node
        current = next_node         # Updates current to the next soldier
        num_soldiers -= 1           # Updates how many soldiers are alive

    print(current.data)         # Loop finishes when there is only ONE remaining

''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()
