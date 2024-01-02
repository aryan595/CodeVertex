import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def rock_paper_scissors():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = input("Enter your choice (1/2/3/4): ")
        
        if user_choice == '4':
            print("\nGame Over. Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

        if user_choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        user_choice = choices[int(user_choice) - 1]

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"\nResult: {result}")

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Scores - You: {user_score} | Computer: {computer_score}")

rock_paper_scissors()
