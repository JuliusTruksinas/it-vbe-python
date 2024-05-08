# Task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
CITY_NAME_LENGTH = 20
COUNTY_NAME_LENGTH = 13
MIN_CITY_POPULATION = "min_city_population"
COUNTY_POPULATION = "county_population"

def main():
    counties = read_data_file()
    sorted_counties = sort_by_min_city_population_and_name(counties)
    write_results_to_a_file(sorted_counties)

# This function read the data file and returns 
def read_data_file():
    counties = {}

    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for line in data_file.read().strip().split("\n")[1:]:
            county_name = line[CITY_NAME_LENGTH: CITY_NAME_LENGTH + COUNTY_NAME_LENGTH]
            population = int(line[CITY_NAME_LENGTH + COUNTY_NAME_LENGTH:])
            found_county = counties.get(county_name, {COUNTY_POPULATION: 0, MIN_CITY_POPULATION: None})
            found_county[COUNTY_POPULATION] += population
            if found_county[MIN_CITY_POPULATION] == None or population < found_county[MIN_CITY_POPULATION]:
                found_county[MIN_CITY_POPULATION] = population
            counties[county_name] = found_county

    return counties

# This function sorts the counties ascendingly by two keys:
# 1) by the minimum population that is in a city and is associated with that county
# 2) by the county name alphabetically  
def sort_by_min_city_population_and_name(counties):
    return sorted(counties.items(), key=lambda item: (item[1][MIN_CITY_POPULATION], item[0]))

# This function writes the results in a file as specified in the task
def write_results_to_a_file(sorted_counties):
    final_results = f"{len(sorted_counties)}\n"
    for county_name, county_data in sorted_counties:
        final_results += f"{county_name}{county_data[MIN_CITY_POPULATION]} {county_data[COUNTY_POPULATION]}\n"

    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip())

main()