# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
NAME_LENGTH = 20
NAME = "name"
NUMBER = "number"
TIME_IN_SECONDS = "time_in_seconds"
GENDER = "gender"
MALE = "male"
FEMALE = "female"
TARGET_HITS = "target_hits"
MAXIMUM_SHOTS = 5
TIME_TO_FINIS_IN_SECONDS = "time_to_finish_in_seconds"
FEMALE_LABEL = "Merginos"
MALE_LABEL = "Vaikinai"

def main():
    all_participants, finishers = read_data_file()
    finishing_participants = calculate_finishers_times(all_participants, finishers)
    male_finishers, female_finishers = seperate_males_and_females(finishing_participants)
    write_results_to_a_file(male_finishers, female_finishers)

# this function returns the participant's gender based on their number
# female number start with 1, male number starts with 2 
def get_gender(number):
    if str(number)[0] == '1':
        return FEMALE
    return MALE

# this function reads the data file and returns all participants and those that finished the race seperately
def read_data_file():
    all_participants = []
    finishers = []
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        number_of_participants = int(data_file.readline().strip())
        for _ in range(number_of_participants):
            participant = data_file.readline().strip()
            name = participant[:NAME_LENGTH]
            number, hours, minutes, seconds = [int(d) for d in participant[NAME_LENGTH:].split()]
            time_in_seconds = hours * 60 * 60 + minutes * 60 + seconds
            all_participants.append({NAME: name, NUMBER: number, TIME_IN_SECONDS: time_in_seconds, GENDER: get_gender(number)})

        number_of_finishers = int(data_file.readline().strip())
        for _ in range(number_of_finishers):
            participant = data_file.readline().strip()
            number, hours, minutes, seconds, *target_hits = [int(d) for d in participant.split()]
            time_in_seconds = hours * 60 * 60 + minutes * 60 + seconds
            finishers.append({ NUMBER: number, TIME_IN_SECONDS: time_in_seconds, TARGET_HITS: target_hits, GENDER: get_gender(number)})
    
    return all_participants, finishers

# this function calculates the penalty in seconds based on the target hits of a participant
def calculate_penalty_in_seconds(target_hits):
    penalty_minutes = sum([MAXIMUM_SHOTS - shot for shot in target_hits])
    return penalty_minutes * 60

# this function returns the participant with his data or None if he was not found based on the finisher number
def find_finishing_participant(all_participants, finisher):
    for participant in all_participants:
        if participant[NUMBER] == finisher[NUMBER]:
            return participant
    return None

# this function returns only the participants that have successfuly finished and calculates the time it took to finish in seconds
def calculate_finishers_times(all_participants, finishers):
    finishing_participants = []
    for finisher in finishers:
        found_finishing_participant = find_finishing_participant(all_participants, finisher)
        if found_finishing_participant:
            found_finishing_participant[TIME_TO_FINIS_IN_SECONDS] = finisher[TIME_IN_SECONDS] - found_finishing_participant[TIME_IN_SECONDS] + calculate_penalty_in_seconds(finisher[TARGET_HITS])
            finishing_participants.append(found_finishing_participant)
    
    return finishing_participants

# this function separates the male and female finishers
def seperate_males_and_females(all_finisher):
    male_finishers = []
    female_finishers = []

    for finisher in all_finisher:
        if finisher[GENDER] == MALE:
            male_finishers.append(finisher)
        else:
            female_finishers.append(finisher)

    return male_finishers, female_finishers

# this function returns hours, minutes and seconds from seconds
def calculate_h_min_s(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hours, minutes, seconds

# this function writes the results to a file as specified in the task
def write_results_to_a_file(male_finishers, female_finishers):
    final_results = f"{FEMALE_LABEL}\n"
    for female_finisher in female_finishers:
        hours, minutes, seconds = calculate_h_min_s(female_finisher[TIME_TO_FINIS_IN_SECONDS])
        final_results += f"{female_finisher[NUMBER]} {female_finisher[NAME]}{hours} {minutes} {seconds}\n"
    
    final_results += f"{MALE_LABEL}\n"
    for male_finisher in male_finishers:
        hours, minutes, seconds = calculate_h_min_s(male_finisher[TIME_TO_FINIS_IN_SECONDS])
        final_results += f"{male_finisher[NUMBER]} {male_finisher[NAME]}{hours} {minutes} {seconds}\n"
    
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip())

main()