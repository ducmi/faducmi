import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    k =None

    print("this is a rock, paper, scissors game!")
    while k not in choices:
       k = input("what is your choice?: ").lower()

    if k == computer:
        print("computer: ", computer)
        print("player:", k)
        print("tie!")
    elif k == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player:", k)
            print ("you lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player:", k)
            print ("you won!")
    elif k == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player:", k)
            print ("you lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player:", k)
            print ("you won!")
    elif k == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player:", k)
            print ("you lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player:", k)
            print ("you won!")
    play_again = input("do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print ("Bye")



#if k = rock:
    
#print(computer)