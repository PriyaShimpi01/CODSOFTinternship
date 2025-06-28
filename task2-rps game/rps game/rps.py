import random

def play_game():
    print("="*40)
    print("    Welcome to Rock, Paper, Scissors!")
    print("="*40)
    print("Instructions:")
    print(" - Type rock, paper, or scissors to play")
    print(" - Type quit to exit the game anytime\n")

    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    while True:
        computer_choice = random.choice(choices)

        user_choice = input("Your choice (rock/paper/scissors): ").lower()

        if user_choice == "quit":
            print("\n👋 Thanks for playing!")
            print(f"Final Score - You: {player_score}, Computer: {computer_score}")
            break

        if user_choice not in choices:
            print("❌ Invalid choice. Please try again.\n")
            continue

        print(f"\n✅ You chose: {user_choice}")
        print(f"🤖 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("🤝 It's a tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win this round!\n")
            player_score += 1
        else:
            print("😞 You lose this round!\n")
            computer_score += 1

        print(f"🏆 Score => You: {player_score} | Computer: {computer_score}\n")
        print("-"*40)

if __name__ == "__main__":
    play_game()
