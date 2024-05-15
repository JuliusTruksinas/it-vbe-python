# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
EXERCISE_NAME_LENGTH = 14
DAY_TIME_LENGTH = 7
TOTAL_DAY_COUNT = "total_day_count"
TOTAL_MINUTES_SPENT = "total_minutes_spent"
MORNING = "Rytas  "
DAY = "Diena  "
EVENING = "Vakaras"

def main():
    exercises = read_data_file()
    write_results_to_a_file(exercises)

# this function reads the next integer from a file
def read_next_integer(file):
    number = ''
    while True:
        char = file.read(1)
        if not char or char.isspace():  # End of file or space
            if number:  # If we have collected any digits
                return int(number)
            if not char:  # End of file
                return None
        elif char.isdigit():
            number += char

# this function reads the data file and returns all of the exercises in a dict:
# key: exercise name; value: dictionary of data about that exercise
def read_data_file():
    exercises = {}
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        days_count = int(data_file.readline().strip())
        for _ in range(days_count):
            unique_exercises = []

            exercises_count = read_next_integer(data_file)
            for _ in range(exercises_count):
                exercise_name = data_file.read(EXERCISE_NAME_LENGTH)
                data_file.read(1) #skip a space
                day_time = data_file.read(DAY_TIME_LENGTH)
                data_file.read(1) #skip a space
                minutes = read_next_integer(data_file)
                found_exercise = exercises.get(exercise_name, {TOTAL_DAY_COUNT: 0, TOTAL_MINUTES_SPENT: 0, MORNING: 0, DAY: 0, EVENING: 0})
                found_exercise[day_time] += 1
                found_exercise[TOTAL_MINUTES_SPENT] += minutes
                exercises[exercise_name] = found_exercise
                
                if exercise_name not in unique_exercises:
                    unique_exercises.append(exercise_name)
            
            for exercise_name in unique_exercises:
                exercises[exercise_name][TOTAL_DAY_COUNT] += 1
    return exercises

# this function writes the results to a file as specified in the task
def write_results_to_a_file(exercises):
    final_results = ""
    sorted_exercises = sorted(exercises.items(), key=lambda exercise: exercise[0])

    for exercise_name, exercise_data in sorted_exercises:
        final_results += f"{exercise_name} {exercise_data[TOTAL_DAY_COUNT]} {exercise_data[TOTAL_MINUTES_SPENT]}\n"

        if exercise_data[MORNING] > 0:
            final_results += f"{MORNING} {exercise_data[MORNING]}\n"
        if exercise_data[DAY] > 0:
            final_results += f"{DAY} {exercise_data[DAY]}\n"
        if exercise_data[EVENING] > 0:
            final_results += f"{EVENING} {exercise_data[EVENING]}\n"
    
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip("\n"))

main()