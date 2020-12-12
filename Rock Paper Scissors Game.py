import random

computer_score = 0
player_score = 0

def choose_option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock","rock"]:
        user_choice = "r"
    elif user_choice in ["Paper","paper"]:
        user_choice = "p"
    elif user_choice in ["Scissors","scissors"]:
        user_choice = "s"
    else:
        print("Invalid option.Try again!")
        choose_option()
    return user_choice

def computer_option():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = "r"
    elif computer_choice == 2:
        computer_choice = "p"
    else:
        computer_choice = "s"
    return  computer_choice

while True:
    print("")
    user_choice = choose_option()
    computer_choice = computer_option()
    print("")

    if user_choice == "r":
        if computer_choice == "r":
            print("You chose rock. The computer chose rock. It's a Tie")
        elif computer_choice == "s":
            print("You chose rock. The computer chose scissors. You win!")
            player_score += 1
        elif computer_choice == "p":
            print("You chose rock. The computer chose paper. You lose")
            computer_score += 1

    if user_choice == "s":
        if computer_choice == "r":
            print("You chose scissors. The computer chose rock. You lose")
            computer_score += 1
        elif computer_choice == "s":
            print("You chose scissors. The computer chose scissors. It's a Tie")
        elif computer_choice == "p":
            print("You chose scissors. The computer chose paper. You win!")
            player_score += 1

    if user_choice == "p":
        if computer_choice == "r":
            print("You chose paper. The computer chose rock. You win!")
            player_score += 1
        elif computer_choice == "s":
            print("You chose paper. The computer chose scissors. You lose")
            computer_score += 1
        elif computer_choice == "p":
            print("You chose paper. The computer chose paper. It's a Tie")

    print("")
    print("Player wins: "+str(player_score))
    print("Computer wins :"+str(computer_score))
    print("")

    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y","y","yes"]:
        pass
    elif user_choice in ["N","n","no"]:
        break
    else:
        break

