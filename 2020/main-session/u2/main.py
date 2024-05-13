# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
NAME_LENGTH = 20
FISH_NAME = "fish_name"
FISH_MASS = "fish_mass"
FISHER_NAME = "fisher_name"
FISH_COUGHT = "fish_cought"
POINTS_FOR_NAME = "points_for_name"
TOTAL_MASS_COUGHT = "total_mass_cought"
MIN_POINTS_FOR_MASS = 10
MAX_POINTS_FOR_MASS = 30
MIN_MASS_TO_GET_MAX_POINTS = 200
POINTS = "points"
PARTICIPANTS_LABEL = "Dalyviai"
COUGHT_FISH_LABEL = "Laimikis"

def main():
    fishers, fishes = read_data_file()
    calculate_points_and_mass(fishers, fishes)
    write_results_to_a_file(fishers, fishes)
    
# this function read the data file and returns all of the fishers' data, and all the fishes that are going to be rated
def read_data_file():
    fishers = []
    fishes = {}

    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        number_of_fishers = int(data_file.readline().strip())
        for _ in range(number_of_fishers):
            fisher = data_file.readline().strip()
            fisher_name = fisher[:NAME_LENGTH]
            number_of_fish = int(fisher[NAME_LENGTH:])
            fish_cought = []

            for _ in range(number_of_fish):
                fish = data_file.readline().strip()
                fish_name = fish[:NAME_LENGTH]
                fish_mass = int(fish[NAME_LENGTH:])
                fish_cought.append({FISH_NAME: fish_name, FISH_MASS: fish_mass})

            fishers.append({FISHER_NAME: fisher_name, FISH_COUGHT: fish_cought, POINTS: 0})
    
        number_of_rated_fish = int(data_file.readline().strip())
        for _ in range(number_of_rated_fish):
            fish = data_file.readline().strip()
            fish_name = fish[:NAME_LENGTH]
            points_for_name = int(fish[NAME_LENGTH:])
            fishes[fish_name] = {POINTS_FOR_NAME: points_for_name, TOTAL_MASS_COUGHT: 0}

    return fishers, fishes

# this function calculates the points gained based on the cought fish mass
def calculate_points_for_mass(mass):
    if mass >= MIN_MASS_TO_GET_MAX_POINTS:
        return MAX_POINTS_FOR_MASS
    return MIN_POINTS_FOR_MASS

# this function goes through every fisher and calculates points for him and at the same time adds the fish mass to total mass cought
def calculate_points_and_mass(fishers, fishes):
    for fisher in fishers:
        for single_fish in fisher[FISH_COUGHT]:
            # print(single_fish)
            fisher[POINTS] += calculate_points_for_mass(single_fish[FISH_MASS])
            fisher[POINTS] += fishes[single_fish[FISH_NAME]][POINTS_FOR_NAME]
            fishes[single_fish[FISH_NAME]][TOTAL_MASS_COUGHT] += single_fish[FISH_MASS]

# this function writes the results to a file as specified in the tas
def write_results_to_a_file(fishers, fishes):
    final_results = f"{PARTICIPANTS_LABEL}\n"
    
    sorted_fishers = sorted(fishers, key=lambda fisher: [-fisher[POINTS], fisher[FISHER_NAME]])
    for fisher in sorted_fishers:
        final_results += f"{fisher[FISHER_NAME]} {fisher[POINTS]}\n"

    sorted_fishes = sorted(fishes.items(), key=lambda item: [-item[1][TOTAL_MASS_COUGHT], item[0]])
    final_results += f"{COUGHT_FISH_LABEL}\n"
    for fish, fish_data in sorted_fishes:
        final_results += f"{fish} {fish_data[TOTAL_MASS_COUGHT]}\n"

    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip())

main()