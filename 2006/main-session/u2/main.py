# task constants
DATA_FILE = "Duom2.txt"
RESULTS_FILE = "Rez2.txt"
STOP_NAME_LENGTH = 15
HOURS_LABEL = "val."
MINUTES_LABEL = "min."
STOP_NAME = "stop_name"
DISTANCE = "distance"
ARRIVAL_TIME_IN_MINUTES = "arrival_time_in_minutes"

def main():
    time_in_minutes, speed_km_per_min, stops = read_data_file()
    calculate_arrival_time_for_stops(time_in_minutes, speed_km_per_min, stops)
    write_results_to_a_file(stops)

# this function reads the data file and returns the current time in minutes, bus speed in km/s, and all stops with their distances
def read_data_file():
    stops = []
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        _, speed, hours, minutes = [int(d) for d in data_file.readline().strip().split()]
        time_in_minutes = hours * 60 + minutes
        speed_km_per_min = speed / 60

        for stop_data in data_file.read().strip().split("\n"):
            stop_name = stop_data[:STOP_NAME_LENGTH]
            distance = float(stop_data[STOP_NAME_LENGTH:])
            stops.append({STOP_NAME: stop_name, DISTANCE: distance, ARRIVAL_TIME_IN_MINUTES: 0})
    return time_in_minutes, speed_km_per_min, stops

# this function calculates the arrival time in minutes for each stop
def calculate_arrival_time_for_stops(time_in_minutes, speed_km_per_min, stops):
    for i, stop in enumerate(stops):
        if i == 0:
            stop[ARRIVAL_TIME_IN_MINUTES] += time_in_minutes + (stop[DISTANCE] / speed_km_per_min)
        else:
            stop[ARRIVAL_TIME_IN_MINUTES] += stops[i-1][ARRIVAL_TIME_IN_MINUTES] + (stop[DISTANCE] / speed_km_per_min)

# this function converts minutes to hours and minutes, and rounds the minutes
def convert_mins_to_hours_and_minutes(minutes):
    return int(minutes // 60), int(minutes % 60 // 1)

# this function writes the results to a file as specified in the task
def write_results_to_a_file(stops):
    final_results = ""
    for stop in stops:
        hours, minutes = convert_mins_to_hours_and_minutes(stop[ARRIVAL_TIME_IN_MINUTES])
        final_results += f"{stop[STOP_NAME]}{hours} {HOURS_LABEL} {minutes} {MINUTES_LABEL}\n"
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip())

main()