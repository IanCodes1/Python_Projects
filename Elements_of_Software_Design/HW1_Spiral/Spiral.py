#  File: Spiral.py
#  Student Name: Ian Salinas


import sys


class NegativeError(Exception):
    pass


class RangeError(Exception):
    pass


# Input: in_data - handle to the input file
# Output: integer size of the spiral, odd integer between 1 and 100
def get_dimension(in_data):
    '''##### ADD CODE HERE #####'''
    # readline grabs first line found in "in_data" #strip gets rid of whitespace
    spiral_size = in_data.readline().strip()

    try:
        spiral_size = int(spiral_size)
        if spiral_size not in range(1, 100):
            raise RangeError
        else:
            if spiral_size % 2 == 0:
                spiral_size += 1
            return spiral_size

    except ValueError:
        print("Invalid spiral size")
        return -1
    except RangeError:
        print("Invalid spiral size")
        return -1


# Input: n - size of spiral
# Output: returns a 2-D list representing a spiral
def create_spiral(n):
    '''##### ADD CODE HERE #####'''
    # Creates spiral utilizing list comprehension
    spiral = [[0 for r in range(n)] for c in range(n)]

    # Finds the center of any spiral given any n
    row = n // 2
    column = n // 2

    # Increments the position of the value
    move = 1

    # Starting value of the center of the spiral
    value = 1

    # Assigns the value to the given spiral indices [row,column]
    spiral[row][column] = value

    # Increments the value
    value = value + 1

    # Runs spiral until it reaches the corner value (n**2)
    while value <= n**2:
        # right move ~ (0,1)
        for v in range(move):
            if value > n ** 2:
                break
            column += 1

            spiral[row][column] = value
            value += 1

        # down move ~ (1,0)
        for v in range(move):
            if value > n ** 2:
                break
            row += 1

            spiral[row][column] = value
            value += 1

        move += 1
        # left move ~ (0,-1)
        for v in range(move):
            if value > n ** 2:
                break
            column -= 1

            spiral[row][column] = value
            value += 1

        # move up ~ (-1,0)
        for v in range(move):
            if value > n ** 2:
                break
            row -= 1

            spiral[row][column] = value
            value += 1
        move += 1

    return spiral


# Added function to check if a number is in the spiral... or not in the spiral.
def in_spiral(spiral, number):
    for row in spiral:
        if number in row:
            return True
    return False


# Input: in_data - handle to input file
#        spiral - the number spiral
# Output: calls method for each integer in file
def print_adjacent_sums(in_data, spiral):
    '''##### ADD CODE HERE #####'''
    in_data = in_data.readlines()
    spiral = spiral[:]

    for nums in in_data:
        try:
            valid_nums = int(nums)
            if valid_nums < 1:
                raise NegativeError
            if not in_spiral(spiral, valid_nums):
                raise RangeError

            adjacent_sum = sum_adjacent_numbers(spiral, valid_nums)
            print(adjacent_sum)

        # Continue skips the current iteration of the loop and moves on to the next iteration
        except ValueError:
            continue
        except TypeError:
            continue
        except NegativeError:
            continue
        except RangeError:
            print(0)


# Input: spiral - the number spiral
#        n - the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    '''##### ADD CODE HERE #####'''
    x_cord = None
    y_cord = None

    for x in range(len(spiral)):
        for y in range(len(spiral[0])):
            if spiral[x][y] == n:
                x_cord = x
                y_cord = y
        if x_cord is not None:
            break

    left_pos = (x_cord, y_cord - 1)  # Left position adjacent to n
    right_pos = (x_cord, y_cord + 1)  # Right position adjacent to n
    up_pos = (x_cord - 1, y_cord)  # Up position adjacent to n
    down_pos = (x_cord + 1, y_cord)  # Down position adjacent to n
    # 1st Corner position adjacent to n
    first_corner = (x_cord - 1, y_cord - 1)
    # 2nd Corner position adjacent to n
    second_corner = (x_cord + 1, y_cord - 1)
    # 3rd Corner position adjacent to n
    third_corner = (x_cord + 1, y_cord + 1)
    # 4th Corner position adjacent to n
    fourth_corner = (x_cord - 1, y_cord + 1)

    positions = [left_pos,
                 right_pos,
                 up_pos,
                 down_pos,
                 first_corner,
                 second_corner,
                 third_corner,
                 fourth_corner]

    sum = 0

    for x, y in positions:

        if 0 <= x < len(spiral) and 0 <= y < len(spiral[0]):
            sum = sum + spiral[x][y]

    return sum


# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
# Input: spiral - the number spiral
# Output: printed spiral
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()


''' ##### DRIVER CODE #####
    ##### Remember to change the debug flag before submitting. '''

# set the input source - change to False before submitting
debug = False
if debug:
    in_data = open('spiral.in')
else:
    in_data = sys.stdin

# get the spiral size from the file
size = get_dimension(in_data)

# if valid spiral size
if size != -1:

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)

    # use following line for debugging only
    # print_spiral(spiral)

    # process and print adjacent sums
    print_adjacent_sums(in_data, spiral)
