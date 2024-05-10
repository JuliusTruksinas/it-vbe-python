# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
NAME_LENGTH = 10
NAME = "name"
DNR_SEQUENCE = "dnr_sequence"
SIMILARITY_COEFFICIENT = "similarity_coefficient"

def main():
    main_sheep_index, sheep = read_data_file()
    calculate_coefficients(main_sheep_index, sheep)
    write_results_to_a_file(main_sheep_index, sheep)

# this function reads the data file and returns ...
def read_data_file():
    sheep = []
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        data_file.readline()
        main_sheep_index = int(data_file.readline().strip()) - 1
        for line in data_file.read().strip().split("\n"):
            sheep_name = line[:NAME_LENGTH]
            dnr_sequence = [d for d in line[NAME_LENGTH:].strip()]
            sheep.append({NAME: sheep_name, DNR_SEQUENCE: dnr_sequence})
    return main_sheep_index, sheep

# This function calculates the similarity coefficient for each sheep based on the main sheep's dnr sequence
def calculate_coefficients(main_sheep_index, sheep):
    main_sheep_dnr_sequence = sheep[main_sheep_index][DNR_SEQUENCE]
    for i, single_sheep in enumerate(sheep):
        if i == main_sheep_index:
            continue

        similarity_coefficient = 0
        for i, d in enumerate(single_sheep[DNR_SEQUENCE]):
            if d == main_sheep_dnr_sequence[i]:
                similarity_coefficient += 1

        single_sheep[SIMILARITY_COEFFICIENT] = similarity_coefficient

# this function writes the results to a file as specified in the task
def write_results_to_a_file(main_sheep_index, sheep):
    main_sheep_name = sheep[main_sheep_index][NAME]
    final_results = f"{main_sheep_name}\n"
    secondary_sheep = [single_sheep for i, single_sheep in enumerate(sheep) if i != main_sheep_index]
    sorted_sheep = sorted(secondary_sheep, key=lambda single_sheep: [-single_sheep[SIMILARITY_COEFFICIENT], single_sheep[NAME]])

    for single_sheep in sorted_sheep:
        final_results += f"{single_sheep[NAME]} {single_sheep[SIMILARITY_COEFFICIENT]}\n"
    
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip())

main()