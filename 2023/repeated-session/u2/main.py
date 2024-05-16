# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
NAME_LENGTH = 13
ROCK = "A"
PAPER = "P"
SCISSORS = "Z"
MOVES = "moves"
WINS = "wins"
LOSSES = "losses"
TIES = "ties"
WIN_LOSS_RATIO = "win_loss_ratio"

def main():
    players = read_data_file()
    compare_players_to_each_other(players)
    calculate_players_win_loss_ratio(players)
    write_results_to_a_file(players)

# this function reads the data file and returns a dictionary of players:
# key: player name, value: dictionary with player data
def read_data_file():
    players = {}
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for line in data_file.read().strip().split("\n")[1:]:
            name = line[:NAME_LENGTH]
            moves = line[NAME_LENGTH+1:].split()
            players[name] = {MOVES: moves, WINS: 0, LOSSES: 0, TIES: 0}
    return players

# this function decides which player won the round and returns 1 for player1, 2 for player2 and 0 if it's a tie
def decide_round_winner(player1_move, player2_move):
    if player1_move == player2_move:
        return 0
    if player1_move == ROCK and player2_move == SCISSORS:
        return 1
    if player1_move == PAPER and player2_move == ROCK:
        return 1
    if player1_move == SCISSORS and player2_move == PAPER:
        return 1
    return 2

# this function compares each player to one another
def compare_players_to_each_other(players):
    players_data = list(players.values())
    for i in range(len(players_data)):
        for j in range(i+1, len(players_data)):
            compare_players(players_data[i], players_data[j])

# this function calculates each players win loss ration
def calculate_players_win_loss_ratio(players):
    players_data = players.values()
    for player_data in players_data:
        player_data[WIN_LOSS_RATIO] = f"{player_data[WINS] / player_data[LOSSES]:.2f}"

# this function compares two players, calculates each ones wins, losses and ties with each other
def compare_players(player1_data, player2_data):
    for i in range(len(player1_data[MOVES])):
        round_winner = decide_round_winner(player1_data[MOVES][i], player2_data[MOVES][i])
        if round_winner == 1:
            player1_data[WINS] += 1
            player2_data[LOSSES] += 1
        elif round_winner == 2:
            player2_data[WINS] += 1
            player1_data[LOSSES] += 1
        else:
            player2_data[TIES] += 1
            player1_data[TIES] += 1

# this function writes the results to a file as specified in the tas
def write_results_to_a_file(players):
    final_results = ""
    sorted_players = sorted(players.items(), key=lambda item: item[1][WIN_LOSS_RATIO], reverse=True)

    for player_name, player_data in sorted_players:
        final_results += f"{player_name} {player_data[WIN_LOSS_RATIO]} {player_data[TIES]}\n"
    
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip("\n"))

main()