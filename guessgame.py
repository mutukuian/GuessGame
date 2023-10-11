
# lives = 3

# players = 2

# level = 1

# def playerLives(lives):
#     if lives > 3:
#         return True
#     else:
#         return False
    
# def endOfGames()
    

import random

# Initialize game variables
player_lives = 3
max_games = 5
current_game = 0
current_level = 1

# Dictionary of words and their explanations for each level
levels = {
    1: {
        "cat": "A furry animal that says 'meow'",
        "sun": "A bright, hot object in the sky",
        "dog": "A loyal pet that says 'woof'"
    },
    # Add more levels and words as needed
}

# Function to play a game at the current level
def play_game():
    global player_lives, current_game, current_level
    current_game += 1
    word = random.choice(list(levels[current_level].keys()))
    explanation = levels[current_level][word]
    
    print(f"\nGame {current_game} - Level {current_level}")
    print(f"Explain the word to Player 2: {explanation}")
    
    attempts = 3  # Player 2 has 3 attempts to guess
    while attempts > 0:
        guess = input("Player 2, guess the word: ").lower()
        if guess == word:
            print("Correct! You guessed the word.")
            break
        else:
            print("Incorrect guess. Try again.")
            attempts -= 1
    else:
        player_lives -= 1
        print(f"Out of attempts. Player 2 loses a life. Lives left: {player_lives}")

# Main game loop
while current_game < max_games and player_lives > 0:
    play_game()
    if current_game % 3 == 0:  # Check if it's time to advance to the next level
        current_level += 1
        print(f"\nCongratulations! You've advanced to Level {current_level}.")
        input("Press Enter to continue...")
        
# Game over
if player_lives > 0:
    print("Congratulations! You've won the game!")
else:
    print("Game over. You've run out of lives.")

print("Thanks for playing!")
