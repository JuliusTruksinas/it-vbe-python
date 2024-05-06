# Task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"
POINTS_FOR_1_WINNER = 4
POINTS_FOR_2_WINNERS = 2

def main():
    votes = [0] * 3
    points = [0] * 3

    company_sectors, director_points = read_data_file()

    for company_sector in company_sectors:
        calculate_points(company_sector, points)
        calculate_votes(company_sector, votes)
    
    add_directors_points(director_points, points)
    winning_logo_number = points.index(max(points)) + 1
    write_results_to_a_file(votes, points, winning_logo_number)

# This function reads the data file and returns the points awarded by different sectors and the director
def read_data_file():
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        company_sectors = []
        lines = data_file.read().strip().split("\n")
        for line in lines[1:-1]:
            company_sectors.append([int(d) for d in line.split()])
        director_points = [int(d) for d in lines[-1].split()]
    return company_sectors, director_points

# This function adds votes to a logo gained by 1 sector
def calculate_votes(company_sector, votes):
    for i, count in enumerate(company_sector):
        votes[i] += count

# This function adds points to a logo gained by 1 sector
def calculate_points(company_sector, points):
    maximum_points = max(company_sector)
    logos_with_max_points = [i for i, el in enumerate(company_sector) if el == maximum_points]
    if len(logos_with_max_points) == 1:
        points[logos_with_max_points[0]] += POINTS_FOR_1_WINNER
    elif len(logos_with_max_points) == 2:
        points[logos_with_max_points[0]] += POINTS_FOR_2_WINNERS
        points[logos_with_max_points[1]] += POINTS_FOR_2_WINNERS

# This function adds points to a logo gained by the director
def add_directors_points(director_points, points):
    maximum_points = max(points)
    maximum_points_count = points.count(maximum_points)
    if maximum_points_count != 1:
        for i in range(len(points)):
            points[i] += director_points[i]

# This function writes the results to a file as specified in the task
def write_results_to_a_file(votes, points, winning_logo_number):
    final_results = f"{' '.join([str(d) for d in votes])}\n{' '.join([str(d) for d in points])}\n{winning_logo_number}"
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results)
main()