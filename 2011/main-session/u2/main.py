# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
PAIR_NAMES_LENGTH = 20
TOTAL_SCORE = "total_score"
PAIR_NAME = "pair_name"
TECHNICAL_POINTS = "technical_points"
ARTISTICAL_POINTS = "artistical_points"

def main():
    pairs = read_data_file()
    calculate_pairs_total_points(pairs)
    write_results_to_a_file(pairs)

# this function reads the data file and returns a list of pairs, each pair is a dictionary, that has pair names, technical points and artistical points
def read_data_file():
    pairs = []
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        pairs_count, _ = [int(d) for d in data_file.readline().strip().split()]
        for _ in range(pairs_count):
            pair_name = data_file.readline()[:PAIR_NAMES_LENGTH]
            technical_points = [int(d) for d in data_file.readline().strip().split()]
            artistical_points = [int(d) for d in data_file.readline().strip().split()]
            pairs.append({PAIR_NAME: pair_name, TECHNICAL_POINTS: technical_points, ARTISTICAL_POINTS: artistical_points})
    return pairs

# this function calculates the points gained from a category ex: technical, artistical
def calculate_points_for_category(category_points):
    category_points_copy = category_points[:]
    minimum = min(category_points_copy)
    maximum = max(category_points_copy)

    if minimum == maximum:
        return sum(category_points_copy[2:])

    category_points_copy.remove(minimum)
    category_points_copy.remove(maximum)

    return sum(category_points_copy)
    
# this function calculates the total points of each pair
def calculate_pairs_total_points(pairs):
    for pair in pairs:
        pair[TOTAL_SCORE] = calculate_points_for_category(pair[TECHNICAL_POINTS]) + calculate_points_for_category(pair[ARTISTICAL_POINTS])

# this function writes the restulst to a file as specified in the task
def write_results_to_a_file(pairs):
    final_results = ""

    sorted_pairs = sorted(pairs, key=lambda pair: pair[TOTAL_SCORE], reverse=True)
    for pair in sorted_pairs:
        final_results += f"{pair[PAIR_NAME]} {pair[TOTAL_SCORE]}\n"

    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip())

main()