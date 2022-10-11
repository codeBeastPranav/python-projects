#rock paper scissors
import random

choice_list = ["rock", "paper", "scissors"]
#random_one = random.choice(choice_list)

#main function
        

play_or_no = input("do you want to play rock paper scissors(yes/no): ")
if play_or_no == "yes":
    #main_function()
    run = True
    while run:
        random_one = random.choice(choice_list)
        user_input = input("enter your choice(R/P/S): ")
        if user_input ==  "R":
            if random_one == "rock":
                print("it is a tie")
            elif random_one == "paper":
                print("you lose")
            elif random_one == "scissors":
                print("you win")
            else:
                pass

        elif user_input == "P":
            if random_one == "rock":
                print("you win")
            elif random_one == "paper":
                print("its a tie")
            elif random_one == "scissors":
                print("you lose")
            else:
                pass

        elif user_input == "S":
            if random_one == "rock":
                print("you lose")
            elif random_one == "paper":
                print("you win")
            elif random_one == "scissors":
                print("its a tie")
            else:
                pass
        elif user_input == "end":
            print("thank you for playing.")
            break

        else:
            print("invalid input. try again")

        

elif play_or_no == "no":
    print("thank you")

else:
    print("invalid input.")