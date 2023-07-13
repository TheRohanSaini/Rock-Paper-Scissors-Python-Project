import random

objects = ("rock","paper","scissor")
running=True
while running==True:
    player= None
    computer = random.choice(objects)
    while player not in objects:
        player = input("choose ( rock paper or scissor ) TYPE HERE = ")
    print("COMPUTER CHOOSE =",computer)
    print("YOU CHOOSE =",player)

    if player==computer:
        print("THIS IS TIE!")
    elif player=="rock" and computer == "scissor":
        print("YOU WIN!")
    elif player=="paper" and computer == "rock":
        print("YOU WIN!")
    elif player=="scissor" and computer == "paper":
        print("YOU WIN!")
    else:
        print("YOU LOSS!")
    play_again = input("PLAY AGAIN? (Y/N)").lower()
    if not play_again =="y":
        running=False
print("THANKS FOR PLAYING!")
