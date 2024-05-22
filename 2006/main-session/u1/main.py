# task constants
DATA_FILE = "Duom1.txt"
RESULTS_FILE = "Rez1.txt"

def main():
    total_resistance = read_data_file()
    write_results_to_a_file(total_resistance)

# this function reads the data file and returns the total resistance of the electrical chain
def read_data_file():
    total_resistance = 0

    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for line in data_file.read().strip("\n").split("\n")[1:]:
            _, *resistors = [int(d) for d in line.split()]
            parallel_resistance = calculate_parallel_resistance(resistors)
            total_resistance += parallel_resistance
    
    return total_resistance

# this function calculates the resistance of a parallel circuit
def calculate_parallel_resistance(resistors):
    parallel_resistance = 0
    for resistance in resistors:
        parallel_resistance += 1/resistance
    return pow(parallel_resistance, -1)

# this function writes the results to a file as specified in the task
def write_results_to_a_file(total_resistance):
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(f"{total_resistance:.2f}")

main()