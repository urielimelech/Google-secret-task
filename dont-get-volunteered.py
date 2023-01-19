##########################################

# Don't Get Volunteered!
# ======================

# As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker.
# It's not easy building a doomsday device and ordering the bunnies around at the same time, after all!
# In order to make sure that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories.
# It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor.
# That would be fine if you got to be the rook or the queen, but instead, you have to be the knight.
# Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

# To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters:
# the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.
# The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square
# using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).
# Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution(0, 1)
# Output:
#     3

# Input:
# solution.solution(19, 36)
# Output:
#     1

##########################################

# import time
def solution(src, dest):
    steps_tree = {}
    count = 1
    if src == dest or not 0 <= src <= 63 or not 0 <= dest <= 63:
        return 0
    steps_tree[count] = [valid_steps(src)]
    while not arrive_to_destination(steps_tree[count], dest):
        # time.sleep(3)
        count += 1
        steps_tree[count] = []
        for valid_step in steps_tree[count-1]:
            for step in valid_step:
                steps_tree[count].append(valid_steps(step))
    return count


def check_next_position(position, column, row):
    y = oct(position)[2] if len(oct(position)) == 4 else '0'
    x = oct(position)[3] if len(oct(position)) == 4 else oct(position)[2]
    if 0 <= int(y) + int(column) <= 7 and 0 <= int(x) + int(row) <= 7:
        return int(f"{int(y) + column}{int(x) + row}", 8)
    return None

def valid_steps(pos):
    steps = [
        [2, 1], # step_down_right
        [2, -1], # step_down_left 
        [-2, 1], # step_up_right
        [-2, -1], # step_up_left
        [1, 2], # step_right_down
        [-1, 2], # step_right_up
        [1, -2], # step_left_down
        [-1, -2] # step_left_up
    ]
    valid_steps = []
    for step in steps:
        column = step[0]
        row = step[1]
        next_position = check_next_position(pos, column, row)
        if next_position != None:
            valid_steps.append(next_position)
    return valid_steps

def arrive_to_destination(positions, dest):
    for steps_pos in positions:
        for arrival_pos in steps_pos:
            if arrival_pos == dest:
                return True
    return False

# print(solution(1, 7))
# print(solution(19, 36))
# print(solution(17, 0))
# print(solution(0, 17))
# print(solution(56, 1))
# print(solution(0, 58))
# print(solution(0, 57))
# print(solution(0, 56))
# print(solution(0, 55))
# print(solution(0, 54))
# print(solution(0, 53))
# print(solution(0, 52))
# print(solution(0, 51))
# print(solution(0, 50))
# print(solution(0, 49))