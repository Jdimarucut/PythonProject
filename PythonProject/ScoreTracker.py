#DIMARUCUT,JON PAOLO
#BSCS-CS2C

# Create a score tracker for a three-round game

# Define a class to represent each player
class Player:
    def __init__(self, name):
        self.name = name
        self.round_scores = []

# Function to add players to the game
def add_players(num_players):
    players = []
    for i in range(num_players):
        player_name = input(f"Enter the name for Player {i + 1}: ")
        players.append(Player(player_name))
    return players

# Function to input scores for each player in each round
def add_scores(players, round_number):
    for player in players:
        while True:
            try:
                score = int(input(f"Enter the score for {player.name} in round {round_number} (max 10 points): "))
                if 0 <= score <= 10:
                    player.round_scores.append(score)
                    break
                else:
                    print("Invalid score. Please enter a score between 0 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Function to display scores after each round
def display_scores(players, round_number):
    print(f"Scores after round {round_number}:")
    for player in players:
        print(f"{player.name}: {sum(player.round_scores)} points")

# Function to determine the winner(s) after three rounds
def determine_winner(players):
    max_score = max(sum(player.round_scores) for player in players)
    winners = [player.name for player in players if sum(player.round_scores) == max_score]
    return winners, max_score

# Get the number of players from the user
num_players = int(input("Enter the number of players: "))
players = add_players(num_players)

# Play three rounds
for round_number in range(1, 4):  # Three rounds
    print(f"Round {round_number}")
    add_scores(players, round_number)
    display_scores(players, round_number)

# Determine the winner(s) after three rounds
winners, max_score = determine_winner(players)

# Display the winner(s)
print("\nWinner(s):")
if len(winners) == 1:
    print(f"The winner is {winners[0]} with {max_score} points!")
else:
    print("It's a tie between:")
    for winner in winners:
        print(f"{winner} with {max_score} points!")