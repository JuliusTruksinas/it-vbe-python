# Task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"
YELLOW = "G"
GREEN = "Z"
RED = "R"

def main():
    all_colors = read_data_file()
    made_flag_count = min(all_colors.values()) // 2
    take_away_used_color(all_colors, made_flag_count)
    write_results_to_a_file(all_colors, made_flag_count)

# This function reads the data file and returns how many colors there are in total
def read_data_file():
    all_colors = {YELLOW: 0, GREEN: 0, RED: 0}

    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for line in data_file.read().strip().split("\n")[1:]:
            color, count = line.split()
            count = int(count)
            all_colors[color] += count
    
    return all_colors

# This function removes the colors that have been used to make the flags
def take_away_used_color(all_colors, made_flag_count):
    for color in all_colors:
        all_colors[color] -= made_flag_count * 2

# This function writes the results to a file as specified in the task
def write_results_to_a_file(all_colors, made_flag_count):
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(f"{made_flag_count}\nG = {all_colors[YELLOW]}\nZ = {all_colors[GREEN]}\nR = {all_colors[RED]}")

main()