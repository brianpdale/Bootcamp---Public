import random

games = 5
user_counter = 0
computer_counter = 0
computer_actions = ["rock", "paper", "scissors"]

print("Get ready for Rock Paper Scissors Vs. your computer")
print("The winner is best out of 5 games")
while user_counter < 3 and computer_counter < 3:   
    user_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(computer_actions)
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print(f"Both players chose {user_choice}. It is a tie.")
        print(user_counter, computer_counter)
        continue
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors. You Win!")
            user_counter += 1
            print((user_counter, computer_counter))
        else: 
            print("Paper covers rock. You Lose.")
            computer_counter += 1
            print((user_counter, computer_counter))

    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper. You Win!")
            user_counter += 1
            print((user_counter, computer_counter))
        else: 
            print("Rock smashes scissors. You Lose.")
            computer_counter += 1
            print((user_counter, computer_counter))

    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock. You Win!")
            user_counter += 1
            print((user_counter, computer_counter))
        else: 
            print("scissors cuts paper. You Lose.")
            computer_counter += 1
            print((user_counter, computer_counter))

    if computer_counter == 3:
        print("Computer Wins All!")
        break
    if user_counter == 3:
        print("You Win All!")
        break



