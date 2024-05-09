# Task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
FULL_NAME_LENGTH = 20

def main():
    groups = read_data_file()
    sorted_top_contestants = get_sorted_top_contestants(groups)
    write_results_to_a_file(sorted_top_contestants)

# This function reads the data file and returns a list of groups, where every group is a dict:
# key: contestant name, value: contestant's time in seconds
def read_data_file():
    groups = []

    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        group_count = int(data_file.readline().strip())
        for _ in range(group_count):
            group = {}
            group_size = int(data_file.readline().strip())
            for _ in range(group_size):
                contestant = data_file.readline().strip()
                contestant_name = contestant[:FULL_NAME_LENGTH]
                minutes, seconds = [int(d) for d in contestant[FULL_NAME_LENGTH:].split()]
                
                time_in_seconds = minutes * 60 + seconds
                group[contestant_name] = time_in_seconds
            groups.append(group)
    return groups

# This function gets the top contestants(half of the best contestants out of every group combined)
def get_sorted_top_contestants(groups):
    top_contestants = []
    for group in groups:
        top_contestants_count = len(group) // 2
        sorted_contestants = sorted(group.items(), key=lambda item: item[1])
        top_contestants += sorted_contestants[:top_contestants_count]
    return sorted(top_contestants, key=lambda item: item[1])

# This function writes the results to a data file as specified in the task
def write_results_to_a_file(sorted_top_contestants):
    final_results = ""
    for contestant_name, time_in_seconds in sorted_top_contestants:
        minutes = time_in_seconds // 60
        seconds = time_in_seconds % 60
        final_results += f"{contestant_name}{minutes} {seconds}\n"

    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip())

main()
read_data_file()