# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
X = "x"
Y = "y"
WIDTH = "width"
LENGTH = "length"
RGB_VALUE = "rgb_value"
BOARD_SIZE = 100
INITIAL_BACKGROUND = "255 255 255"

def main():
    board = initialize_board()
    rectangles = read_data_file()
    maximum_x, maximum_y = draw_rectangles_on_board(rectangles, board)
    final_painting = cut_out_painting(maximum_x, maximum_y, board)
    write_results_to_a_file(final_painting, rectangles, maximum_x, maximum_y)

# This functon initializes and returns a 100 X 100 board (two-dimensional list) filled with the value None
def initialize_board():
    board = []
    for _ in range(BOARD_SIZE):
        board.append([None] * BOARD_SIZE)
    return board

# this function reads the data file and returns all of the rectangles and their data in a list
def read_data_file():
    rectangles = []
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for line in data_file.read().strip().split("\n")[1:]:
            x, y, length, width, *rgb_value = [int(d) for d in line.split()]
            rectangles.append({X: x, Y: y, WIDTH: width, LENGTH: length, RGB_VALUE: rgb_value})
    return rectangles

# takes a single rectangle and draws it on the board (puts the rectangles index on every cell that belongs to that rectangle)
def draw_rectangle_on_board(rectangles, rectangle_index, board):
    rectangle = rectangles[rectangle_index]
    maximum_x = 0
    maximum_y = 0

    for y in range(rectangle[Y], rectangle[Y] + rectangle[WIDTH]):
        if y > maximum_y:
            maximum_y = y
        for x in range(rectangle[X], rectangle[X] + rectangle[LENGTH]):
            board[y][x] = rectangle_index
            if x > maximum_x:
                maximum_x = x

    return maximum_x, maximum_y

# This function goes through each rectangle and draws it on the board (puts the rectangles index on every cell that belongs to that rectangle)
def draw_rectangles_on_board(rectangles, board):
    maximum_x = 0
    maximum_y = 0

    for i in range(len(rectangles)):
        rectangle_maximum_x, rectangle_maximum_y = draw_rectangle_on_board(rectangles, i, board)
        if rectangle_maximum_x > maximum_x:
            maximum_x = rectangle_maximum_x
        if rectangle_maximum_y > maximum_y:
            maximum_y = rectangle_maximum_y
    return maximum_x, maximum_y

# This function takes the edge x and y coordinates and cuts out the board to be x(length) X y(height)
def cut_out_painting(maximum_x, maximum_y, board):
    painting = []
    for y in range(maximum_y+1):
        row = []
        for x in range(maximum_x+1):
            row.append(board[y][x])
        painting.append(row)
    return painting

# This function writes the results to a file as specified in the task
def write_results_to_a_file(final_painting, rectangles, maximum_x, maximum_y):
    final_results = f"{maximum_y+1} {maximum_x+1}\n"

    for y in range(len(final_painting)):
        for x in range(len(final_painting[y])):
            if final_painting[y][x] != None:
                final_results += f"{' '.join([str(d) for d in rectangles[final_painting[y][x]][RGB_VALUE]])}\n"
            else:
                final_results += f"{INITIAL_BACKGROUND}\n"
    
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip())

main()
