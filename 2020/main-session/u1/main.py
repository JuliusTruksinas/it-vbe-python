# task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"

def main():
    days = read_data_file()
    max_different_blooming_flower_count = max(days)
    start_index, end_index = find_biggest_interval_indexes(days, max_different_blooming_flower_count)
    start_month, start_day, end_month, end_day = get_dates_from_indexes(start_index, end_index)
    write_results_to_a_file(max_different_blooming_flower_count, start_month, start_day, end_month, end_day)

# this function find the start and end indexes of the first interval that has the most flowers blooming at the same time
def find_biggest_interval_indexes(days, biggest_value):
    start_index = days.index(biggest_value)
    end_index = start_index
    while end_index <= 91 and days[end_index] == biggest_value:
        end_index += 1

    return start_index, end_index - 1

# this function converts an index to a month and a day
def index_to_date(index):
    if (index + 1) > 61:
        month = 8
        day = (index + 1) - 61
    elif (index + 1) > 30:
        month = 7
        day = (index + 1) - 30
    else:
        month = 6
        day = index + 1

    return month, day

# this function returns the start month, start day, end month, end day of the biggest interval indexes
def get_dates_from_indexes(start_index, end_index):
    start_month, start_day = index_to_date(start_index)
    end_month, end_day = index_to_date(end_index)
    return start_month, start_day, end_month, end_day

# this function reads the data file and returns a list that has a length of 92 and is initialized to 0
# this list represents the 92 days of summer and the value in each index shows how many flowers are blooming at the same time on that particular day
def read_data_file():
    days = [0] * 92

    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for line in data_file.read().strip().split("\n")[1:]:
            _, start_month, start_day, end_month, end_day = [int(d) for d in line.split()]
            fill_days(days, start_month, start_day, end_month, end_day)
    
    return days

# this function converts a date(month and day) to an index
def date_to_index(month, day):
    if month == 6:
        return day - 1
    
    if month == 7:
        return (30 + day) - 1
    
    return (61 + day) - 1

# this function goes through all of the indexes that are between the given days and increments all of the days by 1
def fill_days(days, start_month, start_day, end_month, end_day):
    start_index = date_to_index(start_month, start_day)
    end_index = date_to_index(end_month, end_day)

    while start_index <= end_index:
        days[start_index] += 1
        start_index += 1

# this function writes the results to a file as specified in the task
def write_results_to_a_file(max_different_blooming_flower_count, start_month, start_day, end_month, end_day):
    final_results = f"{max_different_blooming_flower_count}\n{start_month} {start_day}\n{end_month} {end_day}"
    
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results)

main()