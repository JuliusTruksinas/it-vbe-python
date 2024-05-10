# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
FULL_NAME_LENGTH = 20
FULL_NAME = "full_name"
TIME_IN_SECONDS = "time_in_seconds"
TIME_ON_TRACK_IN_SECONDS = "time_on_track_IN_seconds"

def main():
    all_participants, final_participants = read_data_file()
    calculate_time_spent_on_track(all_participants, final_participants)
    write_results_to_a_file(final_participants)

# this function finds and returns a participant out of a list or if not found returns None
def find_participant(participant_to_find, participants):
    for participant in participants:
        if participant[FULL_NAME] == participant_to_find[FULL_NAME]:
            return participant
    return None

# this function goes through each finisher and calculates their time in seconds
def calculate_time_spent_on_track(all_participants, final_participants):
    for final_participant in final_participants:
        found_participant = find_participant(final_participant, all_participants)
        if found_participant != None:
            final_participant[TIME_ON_TRACK_IN_SECONDS] = final_participant[TIME_IN_SECONDS] - found_participant[TIME_IN_SECONDS]

# this function returns a participant as a dict that holds the name of the participant and the current time
def parse_participant_line(participant_line):
    full_name = participant_line[:FULL_NAME_LENGTH]
    hours, minutes, seconds = [int(d) for d in participant_line[FULL_NAME_LENGTH:].split()]
    time_in_seconds = hours * 60 * 60 + minutes * 60 + seconds
    return {FULL_NAME: full_name, TIME_IN_SECONDS: time_in_seconds}

# this function reads the data file and returns the all the participants, and those that finished the race
def read_data_file():
    all_participants = []
    final_participants = []
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        participants_count = int(data_file.readline().strip())
        for _ in range(participants_count):
            participant = parse_participant_line(data_file.readline())
            all_participants.append(participant)
        
        final_participants_count = int(data_file.readline().strip())
        for _ in range(final_participants_count):
            participant = parse_participant_line(data_file.readline())
            final_participants.append(participant)

    return all_participants, final_participants

# this function writes the results to a file as specified in the task
def write_results_to_a_file(final_participants):
    final_results = ""
    sorted_final_participants = sorted(final_participants, key=lambda participant: [participant[TIME_ON_TRACK_IN_SECONDS], participant[FULL_NAME]])
    for participant in sorted_final_participants:
        minutes = participant[TIME_ON_TRACK_IN_SECONDS] // 60
        seconds = participant[TIME_ON_TRACK_IN_SECONDS] % 60
        final_results += f"{participant[FULL_NAME]} {minutes} {seconds}\n"

    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip())

main()