# Task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
BUS_STOP_NAME_LENGTH = 20

def main():
    buses = read_data_file()
    write_results_to_a_file(buses)

# This function reads the data file and returns all the bus numbers and the stop names that the buses visit
def read_data_file():
    # key: bus number; value: bus stop names that this bus visits
    buses = {}

    with open(DATA_FILE, "r", encoding="utf-8") as results_file:
        for line in results_file.read().strip().split("\n")[1:]:
            bus_stop_name = line[:BUS_STOP_NAME_LENGTH]
            bus_numbers = [int(d) for d in line[BUS_STOP_NAME_LENGTH:].strip().split()]
            for bus_number in bus_numbers[1:]:
                found_bus = buses.get(bus_number, [])
                found_bus.append(bus_stop_name)
                buses[bus_number] = found_bus
    return buses

# This function finds and returns the biggest route length
def get_biggest_route_length(buses):
    biggest_route = 0
    for route in buses.values():
        if len(route) > biggest_route:
            biggest_route = len(route)
    return biggest_route

# This function finds and returns the smallest bus number that has the biggest route
def get_smallest_bus_number_with_biggest_route(buses):
    biggest_route = get_biggest_route_length(buses)
    buses_with_biggest_route = []

    for bus_number, route in buses.items():
        if len(route) == biggest_route:
            buses_with_biggest_route.append(bus_number)

    return min(buses_with_biggest_route)

# This function writes the results to a data file as specified in the task
def write_results_to_a_file(buses):
    smallest_bus_number_with_biggest_route = get_smallest_bus_number_with_biggest_route(buses)
    
    final_results = f"{smallest_bus_number_with_biggest_route}\n"
    bus_stop_names = buses[smallest_bus_number_with_biggest_route]

    for i, bus_stop_name in enumerate(bus_stop_names):
        final_results += f"{bus_stop_name}"
        if len(bus_stop_names) - 1 > i:
            final_results += "\n"
        
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results)

main()