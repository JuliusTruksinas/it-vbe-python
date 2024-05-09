# Task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"
PLAY_TIMES = "play_times"
REST_TIMES = "rest_times"
TIMES = "times"

def main():
    # key: player_number, value: {play_times: int[], rest_times: int[], times: int[]}
    players = read_data_file()
    first_5_players_sorted = find_first_5_players_sorted(players)
    player_with_most_play_time, player_with_most_rest_time = find_players_with_most_play_and_rest_time(players) 

    write_results_to_a_file(first_5_players_sorted, player_with_most_play_time, player_with_most_rest_time)

# This function reads data from a file and returns it as a dictionary
def read_data_file():
    players = {}

    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for line in data_file.read().strip().split("\n")[1:]:
            player_number, _, *times = [int(d) for d in line.split()]
            
            # separating play_time from rest_time 
            play_times = [t for t in times if t > 0]
            rest_times = [abs(t) for t in times if t < 0]
            players[player_number] = {PLAY_TIMES: play_times, REST_TIMES: rest_times, TIMES: times}

    return players

# This function finds the players' numbers that were the first to start in an ascending order
def find_first_5_players_sorted(players):
    first_5_players = [item for item in players.items() if item[1][TIMES][0] > 0]
    first_5_players_sorted = sorted(first_5_players, key=lambda item: item[0])
    return [item[0] for item in first_5_players_sorted]

# This function finds the player with most play time and a player with most rest time and returns their numbers and total time.
# If there are multiple players with the highest play or rest time, the function returns a players whose number is the lowest.
def find_players_with_most_play_and_rest_time(players):
    players_with_most_play_time = []
    players_with_most_rest_time = []

    most_time_played_by_player = max([sum(item[1][PLAY_TIMES]) for item in players.items()])
    most_time_rested_by_player = max([sum(item[1][REST_TIMES]) for item in players.items()])

    for player_number, player_data in players.items():
        total_time_played = sum(player_data[PLAY_TIMES])
        total_time_rested = sum(player_data[REST_TIMES])

        if total_time_played >= most_time_played_by_player:
            players_with_most_play_time.append((player_number, total_time_played))
        if total_time_rested >= most_time_rested_by_player:
            players_with_most_rest_time.append((player_number, total_time_rested))
        
    return min(players_with_most_play_time, key=lambda item: item[0]), min(players_with_most_rest_time, key=lambda item: item[0])

# This function writes the final results to a results file, as specified in the exercise
def write_results_to_a_file(first_5_players_sorted, player_with_most_play_time, player_with_most_rest_time):
    final_results = f"{' '.join([str(d) for d in first_5_players_sorted])}\n{' '.join([str(d) for d in player_with_most_play_time])}\n{' '.join([str(d) for d in player_with_most_rest_time])}"
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results)

main()