# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
POINTS_FOR_CORRECT_WORD = 1
POINTS_REDUCTION_FOR_MISTAKE = 10
DISQUALIFICATION_THRESHOLD = 5
CITY_NAME_LENGTH = 15
PARTICIPANT_NAME_LENGTH = 10

NAME = "name"
MISTAKES = "mistakes"
WORDS = "word"
CITY_NAME = "city_name"
TOTAL_POINTS = "total_points"
DISQUALIFIED_LABEL = "Diskvalifikuoti:"

def main():
    participants = read_data_file()
    participants_with_max_points, disqualified_participants, maximum_points = get_best_and_disqualified_participants(participants)
    write_results_to_a_file(participants_with_max_points, disqualified_participants, maximum_points)

# this function reads the data file and returns a list of participants (dictionaries) with their data
def read_data_file():
    participants = []
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        city_count = int(data_file.readline().strip())
        for _ in range(city_count):
            city = data_file.readline().strip()
            city_name = city[:CITY_NAME_LENGTH]
            participant_count = int(city[CITY_NAME_LENGTH+1:])
            for _ in range(participant_count):
                participant = data_file.readline().strip()
                participant_name = participant[:PARTICIPANT_NAME_LENGTH]
                words, mistakes = [int(d) for d in participant[PARTICIPANT_NAME_LENGTH+1:].split()]
                participants.append({NAME: participant_name, WORDS: words, MISTAKES: mistakes, CITY_NAME: city_name})

    return participants

# this function separates the participants that have the highest number of points and those that are disqualified
def get_best_and_disqualified_participants(participants):
    disqualified_participants = []
    maximum_points = 0

    for participant in participants:
        if participant[MISTAKES] >= DISQUALIFICATION_THRESHOLD:
            disqualified_participants.append(participant)
            continue

        points = (participant[WORDS] * POINTS_FOR_CORRECT_WORD) - participant[MISTAKES] * POINTS_REDUCTION_FOR_MISTAKE
        participant[TOTAL_POINTS] = points

        if points > maximum_points:
            maximum_points = points
    participants_with_max_points = [participant for participant in participants if participant[MISTAKES] < DISQUALIFICATION_THRESHOLD and participant[TOTAL_POINTS] == maximum_points]

    return participants_with_max_points, disqualified_participants, maximum_points

# this function writes the results to a file as specified in the task
def write_results_to_a_file(participants_with_max_points, disqualified_participants, maximum_points):
    final_results = f"{maximum_points}\n"
    for participant in sorted(participants_with_max_points, key=lambda p: p[MISTAKES]):
        final_results += f"{participant[NAME]} {participant[CITY_NAME]}\n"
    
    if len(disqualified_participants) > 0:
        final_results += f"{DISQUALIFIED_LABEL}\n"
        for participant in disqualified_participants:
            final_results += f"{participant[NAME]}\n"
    
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip("\n"))

main()