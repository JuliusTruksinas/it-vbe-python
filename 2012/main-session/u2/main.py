# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
NAME_LENGTH = 10
NAME = "name"
DICE_THROWS = "dice_throws"
TOTAL_POINTS = "total_points"

def main():
    gods = read_data_file()
    winning_god = get_the_winning_god(gods)
    write_results_to_a_file(winning_god)

# this function reads the data file and returns a list of gods, each god is a dict containing a name and all the dice throws
def read_data_file():
    gods = []
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for line in data_file.read().strip().split("\n")[1:]:
            name = line[:NAME_LENGTH]
            dice_throws = [int(d) for d in line[NAME_LENGTH:].strip().split()]
            gods.append({NAME: name, DICE_THROWS: dice_throws})
    return gods

# This function returns the winning god based on the rules provided in the task
def get_the_winning_god(gods):
    for god in gods:
        points = 0

        for throw in god[DICE_THROWS]:
            if throw % 2 == 0:
                points += throw
            else:
                points -= throw

        god[TOTAL_POINTS] = points

    highest_points = max(gods, key=lambda god: god[TOTAL_POINTS])[TOTAL_POINTS]
    gods_that_have_highest_points = [god for god in gods if god[TOTAL_POINTS] == highest_points]

    if len(gods_that_have_highest_points) == 1:
        return gods_that_have_highest_points[0]
    
    highest_number_of_even_throws = max([sum([1 for d in god[DICE_THROWS] if d % 2 == 0]) for god in gods_that_have_highest_points])
    gods_that_have_highest_number_of_even_throws = [god for god in gods_that_have_highest_points if sum([1 for d in god[DICE_THROWS] if d % 2 == 0]) == highest_number_of_even_throws]
    
    return gods_that_have_highest_number_of_even_throws[0]

# this function writes the results to a file as specified in the task 
def write_results_to_a_file(winning_god):
    final_results = f"{winning_god[NAME]} {winning_god[TOTAL_POINTS]}"
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results)

main()