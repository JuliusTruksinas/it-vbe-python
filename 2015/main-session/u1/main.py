# Task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"
NUMBER_OF_STUDENTS = 20
NUMBER_OF_PLUMS_PER_GIRL = 10
NUMBER_OF_BOYS = 10
NUMBER_OF_GIRLS = 10

def main():
    girls_ate = read_data_file()
    girls_have = get_how_many_plums_girls_have(girls_ate)
    students_ate = get_how_many_plums_students_ate(girls_have, girls_ate)
    write_results_to_a_file(students_ate)

# This function reads the data file and returns how many plums the girls ate
def read_data_file():
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        return [int(d) for d in data_file.read().strip().split()]

# This function calculates how many plums girls have left after eating some
def get_how_many_plums_girls_have(girls_ate):
    girls_had = [NUMBER_OF_PLUMS_PER_GIRL] * NUMBER_OF_GIRLS
    for i, count in enumerate(girls_ate):
        girls_had[i] -= count
    return girls_had

# This function calculates how many plums all students ate
def get_how_many_plums_students_ate(girls_have, girls_ate):
    students_ate = girls_ate + [0] * NUMBER_OF_BOYS

    for i in range(len(girls_have)):
        j = i + 1
        while girls_have[i] > 0:
            students_ate[j] += 1
            girls_have[i] -= 1
            j += 1
    return students_ate

# This function writes the results to a file as specified in the task
def write_results_to_a_file(students_ate):
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(" ".join([str(d) for d in students_ate]))

main()