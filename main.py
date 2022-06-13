import random
print("Welcome to the Rock, Paper, Scissor game!!!")
user_action = input("pick one: R, P OR S")
possible_output = ["Rock", "Paper", "Scissors"]
computer_action = random.choice(possible_output)

while True:
    if user_action == "R":
        user_action = "Rock"
    elif user_action == "P":
        user_action = "Paper"
    elif user_action == "S":
        user_action = "Scissors"
    elif user_action not in possible_output:
        print("Please pick a valid option!")
        user_action = input("pick one: R, P OR S")

    elif user_action == computer_action:
        print(f"Player((user_action)): CPU((computer_action))")
        print(f"Both players picked (user_action), Wow! a Tie")
        print("Try again")
        user_action = input("pick one: R, P OR S")
        computer_action = random.choice(possible_output)
        continue
    else:
        print(f"Player((user_action)): CPU((computer_action))")

        if user_action == "Rock":
            if computer_action == "Scissors":
                print("Rock smashes scissors! wow you winnnn!")
            else:
                print("Paper covers scissors!You lose!")

        elif user_action == "Paper":
            if computer_action == "Rock":
                print("Paper covers rock!wow you winnnn!")
            else:
                print("Scissors cuts paper!You lose!")

        elif user_action == "Scissors":
            if computer_action == "Paper":
                print("Scissors cut paper!wow you winnnn!")
            else:
                print("Rock smashes scissors!You lose!")

        print("Game Over!!!")
        break
