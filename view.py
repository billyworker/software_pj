import os

def printBoard(chessArrA, chessArrB, den, trap, river):
    os.system('cls')
    print("|----|----|----|----|----|----|----|")
    for y in range(9):
        print("| ", end="")
        for x in range(7):
            printed = False
            for i in range(8):
                if chessArrA[i].inPos(x, y):
                    print(chessArrA[i].getName(), end="")
                    printed = True
                    break
                elif chessArrB[i].inPos(x, y):
                    print(chessArrB[i].getName(), end="")
                    printed = True
                    break
            if not printed:
                if den.isDen(x, y):
                    print("()", end="")  # '()' as den
                    printed = True
                elif trap.isTrap(x, y):
                    print("{}", end="")  # '{}' as trap
                    printed = True
                elif river.isRiver(x, y):
                    print("~~", end="")  # '~~' as river
                    printed = True
            if printed:
                print(" | ", end="")
            else:
                print("   | ", end="")
            if x == 6:
                charMean(y)
        print("|----|----|----|----|----|----|----|")

def charMean(i):
    if i == 0:
        print("{}\t\t{}".format("\"R\" = Rat","\"()\" = Den"))
    elif i == 1:
        print("{}\t\t{}".format("\"C\" = Cat", "\"{}\" = Trap"))
    elif i == 2:
        print("{}\t\t{}".format("\"D\" = Dog", "\"~~\" = River"))
    elif i == 3:
        print("{}".format("\"W\" = Wolf"))
    elif i == 4:
        print("{}".format("\"L\" = Leopard"))
    elif i == 5:
        print("{}".format("\"T\" = Tiger"))
    elif i == 6:
        print("{}".format("\"I\" = Lion"))
    elif i == 7:
        print("{}".format("\"E\" = Elephant"))
    else:
        print()

def remind():
    print()
    print("\"[A/B][chess] [U/D/L/R]\" to control e.g. \"AE U\"")
    print("exit/EXIT to quit, restart/RESTART to reset the game")
    print("Please enter a command:")

def errMessage(errID):
    print()
    if errID == 1:
        print("Incorrect command entered.")
    elif errID == 2:
        print("Incorrect chess entered.")
    elif errID == 3:
        print("Incorrect movement position entered.")
    elif errID == 4:
        print("Movement unsuccessful.")
    elif errID == 5:
        print("Game Ended, please restart or exit.")
    elif errID == 6:
        print("This is not your turn.")

    print("Please enter again:")

def winMessage(player):
    print()
    if player == 'A':
        print("Game Ended, player A win")
    else:
        print("Game Ended, player B win")

    print("\"exit\" to quit the game, \"restart\" to restart the game")
    print("Please enter a command:")
