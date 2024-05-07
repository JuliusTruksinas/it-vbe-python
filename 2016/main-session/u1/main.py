# Task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"

def main():
    bags = read_data_file()
    heaviest_bag = max(bags)

    # way lighter bags are those that weigh 2 or more times less than the heaviest bag 
    way_lighter_bags = [bag for bag in bags if heaviest_bag // bag >= 2]

    write_results_to_a_file(heaviest_bag, len(way_lighter_bags))
    

# This function reads the data file and returns an array of the weight of all of the bags
def read_data_file():
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        return [int(d) for d in data_file.read().strip().split("\n")[1:]]

# This function writes the results to a file as specified in the task
def write_results_to_a_file(heaviest_bag, way_lighter_bags_count):
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(f"{heaviest_bag} {way_lighter_bags_count}")

main()