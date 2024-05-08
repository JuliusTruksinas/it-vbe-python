# Task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
REACHED_GOAL = "pasiektas tikslas   "
SEQUENCE_END = "sekos pabaiga       "
UP, RIGHT, DOWN, LEFT = 1, 2, 3, 4
ONE_STEP = 1

def main():
    start_coordinates, finish_coordinates, direction_sequences = read_data_file()
    write_rezults_to_a_file(start_coordinates, finish_coordinates, direction_sequences)

# This function reads the data file and returns start coordinates, finish coordinates and command sequences
def read_data_file():
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        lines = data_file.read().strip().split("\n")
        start_coordinates = [int(d) for d in lines[0].split()]
        finish_coordinates = [int(d) for d in lines[1].split()]
        direction_sequences = []
        for line in lines[3:]:
            direction_sequences.append([int(d) for d in line.split()][1:])
        return start_coordinates, finish_coordinates, direction_sequences

# This function makes one step and mutates the given coordinates
def move_one_step(current_coordinates, direction):
    if direction == UP:
        current_coordinates[1] += ONE_STEP
    elif direction == DOWN:
        current_coordinates[1] -= ONE_STEP
    elif direction == LEFT:
        current_coordinates[0] -= ONE_STEP
    elif direction == RIGHT:
        current_coordinates[0] += ONE_STEP

# This function goes through direction sequence and returns the final message which can be REACHED_GOAL or SEQUENCE_END
def execute_sequence(current_coordinates, finish_coordinates, direction_sequence):
    coordinate_copy = current_coordinates[:]
    executed_sequence = []
    has_reached_goal = False
    for direction in direction_sequence:
        if coordinate_copy == finish_coordinates:
            has_reached_goal = True
            break
        move_one_step(coordinate_copy, direction)
        executed_sequence.append(direction)

    # this checks if the last made move reached the finish point
    if coordinate_copy == finish_coordinates:
            has_reached_goal = True
    
    execution_message = REACHED_GOAL if has_reached_goal else SEQUENCE_END
    return execution_message, executed_sequence + [len(executed_sequence)]


# This function writes the rezults to a file as specified in the task
def write_rezults_to_a_file(start_coordinates, finish_coordinates, direction_sequences):
    final_results = ""

    for direction_sequence in direction_sequences:
        execution_message, executed_sequence = execute_sequence(start_coordinates, finish_coordinates, direction_sequence)
        final_results += f"{execution_message}{' '.join([str(d) for d in executed_sequence])}\n"

    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip())

main()