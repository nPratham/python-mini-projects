import random

score_card = 0  # Initialize player's score to 0

# Function to determine the result of a game round
def game_logic(computer, human):
    if (computer == human):
        return 0  # Return 0 if it's a draw
    if (computer == 0 and human == 1):
        return -1  # Computer wins: Snake drinks water
    if (computer == 1 and human == 2):
        return -1  # Computer wins: Water douses gun
    if (computer == 2 and human == 0):
        return -1  # Computer wins: Gun kills snake
    return 1  # Human wins in all other cases

# Define choices as 0 (snake), 1 (water), 2 (gun)
elements = [0, 1, 2]

print(f"!it will be 5 game touranment!")  # Start message

# Play 5 rounds
for i in range(1, 6):
    computer = random.choice(elements)  # Random computer choice
    human = int(input(f"Please select one from snake[0],water[1],gun[2]: "))  # User input
    score = game_logic(computer, human)  # Get result of the round

    # Handle different outcomes and update score
    if score == -1:
        score_card = score_card  # No change in score for computer win
        print("Computer Win and your score is: ", score_card)
    elif score == 1:
        score_card += 1  # Increase score if player wins
        print("You Win and your score is: ", score_card)
    elif score == 0:
        score_card = score_card  # No change for draw
        print("its a draw and your score is: ", score_card)

# Print final score after 5 rounds
print(f"Your Final Score is: {score_card}")
