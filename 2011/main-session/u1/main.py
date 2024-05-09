# Task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"
FOR_MEN = 3
FOR_WOMEN = 4
LEFT_HAND = 1
RIGHT_HAND = 2

def main():
    # key: (gender, size); value: { LEFT_HAND: count, RIGHT_HAND: count }
    gloves = read_data()

    # filtering out the men gloves from the women gloves
    gloves_for_men = [item for item in gloves.items() if item[0][0] == FOR_MEN]
    gloves_for_women = [item for item in gloves.items() if item[0][0] == FOR_WOMEN]

    # getting the pairs and remainings of men and women gloves
    women_glove_pairs, women_glove_remaining = calculate_pairs_and_remaining(gloves_for_women)
    men_glove_pairs, men_glove_remaining = calculate_pairs_and_remaining(gloves_for_men)

    # writing the final results to the results file
    final_results = f"{women_glove_pairs}\n{men_glove_pairs}\n{women_glove_remaining}\n{men_glove_remaining}"
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results)

# this function reads the data from the data file
def read_data():
    gloves = {}

    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for eilute in data_file.read().strip().split("\n")[1:]:
            lytis, ranka, dydis = [int(d) for d in eilute.split()]
            rastos_pirstines = gloves.get((lytis, dydis), {LEFT_HAND: 0, RIGHT_HAND: 0})
            rastos_pirstines[ranka] += 1
            gloves[(lytis, dydis)] = rastos_pirstines
    return gloves


def calculate_pairs_and_remaining(gloves):
    pairs = sum([min(item[1][LEFT_HAND], item[1][RIGHT_HAND]) for item in gloves])
    remaining = sum([max(item[1][LEFT_HAND], item[1][RIGHT_HAND]) - min(item[1][LEFT_HAND], item[1][RIGHT_HAND]) for item in gloves])
    return pairs, remaining

main()