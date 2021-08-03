import random


# defines a wrapper function storing:
# number of games payed
# number of games won
# number of games lost
# number of games tied
def rps():

    games = []
    wins = []
    losses = []
    ties = []

    #defines a function for main gameplay
    def moves():

        #chooses opponent's move, 1 for rock,
        #  2 for paper, and 3 for scissors
        x = random.randint(1,3)

        y = (int(input("1 for rock, 2 for paper, 3 for scissors: ")))
        games.append("game")

        print("your opponent has chosen " +(str(x)) +" for their move, and you have chosen " + (str(y))+". ")

        if y != (1 or 2 or 3):
            print("you have to choose either 1, 2, or 3. Please try again. ")
            return moves()
        elif x == y:
            ties.append("win")
            a = (input("It's a TIE! Would you like to play again? "))
            if a == "y":
                return moves()
            elif a == "n":
                print(("you won ")+(str(len(wins)))+(" out of ")+(str(len(games)))+(" games."))
                print(("You suffered ")+(str(len(losses)))+(" losses out of ")+(str(len(games)))+(" games."))
                print(("There were ")+(str(len(ties)))+(" ties out of ")+(str(len(games)))+(" games.\n Thank you for playing, have a great day!"))
        elif (y == 1 and x == 3) or (y == 2 and x == 1) or (y == 3 and x == 2):
            wins.append("win")
            a = (input("You win! Would you like to play again? "))
            if a == "y":
                return moves()
            elif a == "n":
                print(("you won ")+(str(len(wins)))+(" out of ")+(str(len(games)))+(" games."))
                print(("You suffered ")+(str(len(losses)))+(" losses out of ")+(str(len(games)))+(" games."))
                print(("There were ")+(str(len(ties)))+(" ties out of ")+(str(len(games)))+(" games.\n Thank you for playing, have a great day!"))
        elif (y == 1 and x == 2) or (y == 2 and x == 3) or (y == 3 and x ==1):
            losses.append("loss")
            a = (input("So sorry luv, you lost this one. Care to play again? "))
            if a == "y":
                return moves()
            elif a == "n":
                print(("you won ")+(str(len(wins)))+(" out of ")+(str(len(games)))+(" games."))
                print(("You suffered ")+(str(len(losses)))+(" losses out of ")+(str(len(games)))+(" games."))
                print(("There were ")+(str(len(ties)))+(" ties out of ")+(str(len(games)))+(" games.\n Thank you for playing, have a great day!"))

    moves()


rps()
