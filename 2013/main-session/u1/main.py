# Task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"
COMPANY_NAME_LENGTH = 10

def main():
    # comapnies -> {company_name: company_coordinates}
    maximum_distance, companies = read_data_file()
    write_results_to_a_file(companies, maximum_distance)

# This function reads the data from file and returns the maximum_distance, and all companies with their coordinates in a dict
def read_data_file():
    companies = {}

    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        lines = data_file.read().strip().split("\n")
    
    _, maximum_distance = [int(d) for d in lines[0].split()]
    for line in lines[1:]:
        company_name = line[:COMPANY_NAME_LENGTH]
        x, y = [int(d) for d in line[COMPANY_NAME_LENGTH+1:].split()]
        companies[company_name] = (x,y)
    
    return maximum_distance, companies

# This function calculates how many km is needed to travel in order to visit a company and come back to the origin (0,0)
def calculate_distance_to_company(coordinates):
    x, y = coordinates
    return (abs(x) + abs(y)) * 2

# This function calculates, how many companies were visited, what is the total distance traveled, and the last company that was visited
def get_companies_visited_distance_traveled_and_last_company_visited(companies, maximum_distance):
    traveled_distance = 0
    companies_visited = 0
    last_company_visited = None

    for company_name, coordinates in companies.items():
        distance_to_company = calculate_distance_to_company(coordinates)

        if maximum_distance - distance_to_company >= 0:
            traveled_distance += distance_to_company
            companies_visited += 1
            maximum_distance -= distance_to_company
            last_company_visited = company_name
        else:
            break
    
    return companies_visited, traveled_distance, last_company_visited

# This function writes the results to a file as specified in the task
def write_results_to_a_file(companies, maximum_distance):
    final_data = get_companies_visited_distance_traveled_and_last_company_visited(companies, maximum_distance)
    final_results = f"{' '.join([str(d) for d in final_data])}"
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results)

main()