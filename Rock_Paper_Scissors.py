from random import randint

#create a list of play options
f = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = f[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    computer = f[randint(0,2)]

#Define new function
def ng():
    operation = input('''
Do you want to play again?
Yes, No
''')

    if operation == 'Yes':
        #assign a random play to the computer
        computer = f[randint(0,2)]

        player = False

        while player == False:
        #set player to True
            player = input("Rock, Paper, Scissors?")
            if player == computer:
                print("Tie!")
                ng()
            elif player == "Rock":
                if computer == "Paper":
                    print("You lose!", computer, "covers", player)
                    ng()
                else:
                    print("You win!", player, "smashes", computer)
                    ng()
            elif player == "Paper":
                if computer == "Scissors":
                    print("You lose!", computer, "cut", player)
                    ng()
                else:
                    print("You win!", player, "covers", computer)
                    ng()
            elif player == "Scissors":
                if computer == "Rock":
                    print("You lose...", computer, "smashes", player)
                    ng()
                else:
                    print("You win!", player, "cut", computer)
                    ng()
            else:
                print("That's not a valid play. Check your spelling!")
                ng()
            #player was set to True, but we want it to be False so the loop continues
            computer = f[randint(0,2)]
            player == False
    elif operation == 'No':
        Player = True
        print('Thanks for playing!')
    else:
        print('''That's not a valid answer.''')
        ng()
ng()
