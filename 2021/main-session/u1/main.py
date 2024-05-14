# task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"
DAY = "DAY"
TOTAL_TIME_SPENT = "total_time_spent"
MIN_TIME_LABEL = "Minimalus laikas"
DAYS_LABEL = "Dienos"

def main():
    active_days = read_data_file()
    min_time_spent = min(active_days, key=lambda day: day[TOTAL_TIME_SPENT])[TOTAL_TIME_SPENT]
    least_active_days = find_least_active_days(active_days, min_time_spent)
    write_results_to_a_file(min_time_spent, least_active_days)

# this function calculates how many minutes did the man exercise in the morning and in the evening
def calculate_time_spent_in_min(s_m_h, s_m_m, e_m_h, e_m_m, s_e_h, s_e_m, e_e_h, e_e_m):
    morning_exercise_time_seconds =  (e_m_h * 3600 + e_m_m * 60) - (s_m_h * 3600 + s_m_m * 60)
    evening_exercise_time_seconds = (e_e_h * 3600 + e_e_m * 60) - (s_e_h * 3600 + s_e_m * 60)
    return (morning_exercise_time_seconds + evening_exercise_time_seconds) // 60

# this function reads the data file and returns all of the active days(those where the man runs in the morning and in the evening)
def read_data_file():
    active_days = []
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for line in data_file.read().strip().split("\n")[1:]:
            # s_m_h - start morning hour; s_m_m - start morning minutes and so on...
            day_number, s_m_h, s_m_m, e_m_h, e_m_m, s_e_h, s_e_m, e_e_h, e_e_m = [int(d) for d in line.split()]
            if sum([s_m_h, s_m_m, e_m_h, e_m_m]) == 0 or sum([s_e_h, s_e_m, e_e_h, e_e_m]) == 0:
                continue
            active_days.append({DAY: day_number, TOTAL_TIME_SPENT: calculate_time_spent_in_min(s_m_h, s_m_m, e_m_h, e_m_m, s_e_h, s_e_m, e_e_h, e_e_m)})

    return active_days

# this function finds the least active days, which are those where the minimum time was spent on exercising
def find_least_active_days(active_days, min_time_spent):
    least_active_days = []
    for day in active_days:
        if day[TOTAL_TIME_SPENT] == min_time_spent:
            least_active_days.append(day)
    return least_active_days

# this function writes the results to a file as specified in the task
def write_results_to_a_file(min_time_spent, least_active_days):
    final_results = f"{MIN_TIME_LABEL}\n{min_time_spent}\n{DAYS_LABEL}\n"
    final_results += f"{' '.join([str(day[DAY]) for day in least_active_days])}"
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results)

main()