import random

user_wins = 0
user_losses = 0
computer_wins = 0

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw! \U0001F914"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win! \U0001F389"
    else:
        return "You lose! 😢"

while True:
    print("\nRock, Paper, or Scissors?")
    user_action = input("Enter your choice (🪨 rock, 📄 paper, ✂️ scissors): ").lower()
    
    if user_action == "exit":
        print("Exiting the game. See you again! \U0001F44B")
        break

    if user_action not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, scissors, or type 'exit' to end the game.")
        continue

    computer_action = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_action}")

    result = determine_winner(user_action, computer_action)
    print(result)

    if "win" in result:
        user_wins += 1
        print("Congratulations! You are the winner! 🏆")
    elif "lose" in result:
        user_losses += 1
        print("Better luck next time! You lost. 😢")

    print(f"User Wins: {user_wins}, User Losses: {user_losses}, Computer Wins: {computer_wins}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"\nOverall Score:")
        print(f"User Wins: {user_wins}, User Losses: {user_losses}, Computer Wins: {computer_wins}")
        print("See you again! \U0001F44B")
        break
