# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
EXERCISE_NAME_LENGTH = 20

def main():
    exercises = read_data_file()
    write_results_to_a_file(exercises)

# this function reads the data file and returns a dict (key: exercise name, value: total amount of times it was done)
def read_data_file():
    exercises = {}
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for line in data_file.read().strip().split("\n")[1:]:
            exercise_name = line[:EXERCISE_NAME_LENGTH]
            number_of_times_performed = int(line[EXERCISE_NAME_LENGTH+1:])
            exercises[exercise_name] = exercises.get(exercise_name, 0) + number_of_times_performed
    return exercises


# this function writes the results to a file as specified in the task
def write_results_to_a_file(exercises):
    final_results = ""
    sorted_exercises = sorted(exercises.items(), key=lambda item: [-item[1], item[0]])
    
    for exercise_name, number_of_times_performed in sorted_exercises:
        final_results += f"{exercise_name} {number_of_times_performed}\n"
    
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip())

main()