#  File: Work.py
#  Student Name: Ian Salinas
#  Student UT EID: ibs325
#  Partner Name: Nicholas Gonzalez
#  Partner UT EID: ng25878
import sys
import time


# Purpose: Determines how many lines of code will be written
#          before the coder crashes to sleep. Must be implemented
#          using recursion.
# Input: lines_before_coffee - how many lines of code to write before coffee
#        prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written
#         before the coder falls asleep
def sum_series(lines_before_coffee, prod_loss):
    '''##### ADD CODE HERE #####'''    


    while True:     # Loops to find total lines of code WRITTEN before crashing

        if lines_before_coffee <= 0:        # Base Case = number of lines before needing coffee is 0 (or negative)
            return 0
        
        else:
            return (lines_before_coffee) + sum_series(lines_before_coffee // prod_loss , prod_loss)
            # (CURRENT LINES) + (TOTAL LINES) which is given by a recursive call decreasing lines_before_coffee by productivity loss 
    

# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def linear_search(total_lines, prod_loss):
    '''##### ADD CODE HERE #####'''
    

    sum_call_count = 0      # Recieves counter for sum_series calls
    
    for lines_before_coffee in range(1, total_lines + 1):       # Loops through starting lines before coffee, 1 to the total_lines.
        
        written_lines = sum_series(lines_before_coffee, prod_loss)      # Calculates the total lines written with a current starting line
        sum_call_count += 1
         

        if written_lines >= total_lines:
            return lines_before_coffee, sum_call_count      # Returns if the code is not suitable
         
       
    return total_lines, sum_call_count       # Returns starting lines
    

# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def binary_search(total_lines, prod_loss):
    '''##### ADD CODE HERE #####'''


    low = 1     # Starts at lower bound
    high = total_lines      # Sets inital upper bound
    count = 0       # Counts sum_series calls    
    start = high        # Sets variable start to upper bound

    while low <= high:      # Loops until the low and the high meet
        
        mid = (low + high) // 2      
        count += 1
        lines_written = sum_series(mid,prod_loss)       # Receives written lines from the midpoint

        if lines_written < total_lines:                 
            low = mid + 1
    
        else:
            start = mid
            high = mid - 1

    return start, count     # Returns the starting line before coffee and returns count


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''

def main():

    # Open input source
    # Change debug to false before submitting
    debug = False
    if debug:
        in_data = open('work.in')
    else:
        in_data = sys.stdin

    # read number of cases
    line = in_data.readline().strip()
    num_cases = int(line)

    for i in range(num_cases):

        # read one line for one case
        line = in_data.readline().strip()
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(binary_time),
              "seconds")
        print()
    
        
        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(linear_time),
              "seconds")
        print()

        # Comparison
        print("Binary Search was",
              "{0:.1f}".format(linear_time / binary_time),
              "times faster.")
        print()
        print()
    


if __name__ == "__main__":
    main()
    