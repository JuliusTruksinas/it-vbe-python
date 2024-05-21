# task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"

def main():
  days = read_data_file()
  write_results_to_a_file(days)

def read_data_file():
    days = {}
    with open("U1.txt", "r", encoding="utf-8") as duom:
        for line in duom.read().split("\n")[1:]:
            day_data = [int(d) for d in line.split()]

            if len(day_data) == 0:
                continue

            day_number, mushroom_1, mushroom_2, mushroom_3 = day_data[0], day_data[1], day_data[2], day_data[3]
            found_day = days.get(day_number, [0,0,0])
            found_day[0] += mushroom_1
            found_day[1] += mushroom_2
            found_day[2] += mushroom_3

            days[day_number] = found_day
            
    return days

def write_results_to_a_file(days):
    final_results = ""
    sorted_days = sorted(days.items())
    day_with_most_mushrooms = max(sorted_days, key=lambda d: sum(d[1]))[0]

    for day_number, day_data in sorted_days:
        if(sum(day_data) > 0):
            final_results += f"{day_number} {' '.join([str(d) for d in day_data])}\n"

    final_results += f"{day_with_most_mushrooms} {sum(days[day_with_most_mushrooms])}"
    with open("U1rez.txt", "w", encoding="utf-8") as results_file:
        results_file.write(final_results)

main()