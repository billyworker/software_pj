import jungleClass as jc
import view

# storage
chessArrA = []  # chess obj array
chessArrB = []
den = jc.Den()
trap = jc.Trap()
river = jc.River()

chessA = 8
chessB = 8
gameEnd = False
turn = 'A'


# initialization
def init():
    chessArrA.clear()
    chessArrB.clear()
    # rat
    chessArrA.append(jc.Chess(0, 2, 0, 'A', 'R'))
    chessArrB.append(jc.Chess(6, 6, 0, 'B', 'R'))
    # cat
    chessArrA.append(jc.Chess(5, 1, 1, 'A', 'C'))
    chessArrB.append(jc.Chess(1, 7, 1, 'B', 'C'))
    # dog
    chessArrA.append(jc.Chess(1, 1, 2, 'A', 'D'))
    chessArrB.append(jc.Chess(5, 7, 2, 'B', 'D'))
    # wolf
    chessArrA.append(jc.Chess(4, 2, 3, 'A', 'W'))
    chessArrB.append(jc.Chess(2, 6, 3, 'B', 'W'))
    # leopard
    chessArrA.append(jc.Chess(2, 2, 4, 'A', 'L'))
    chessArrB.append(jc.Chess(4, 6, 4, 'B', 'L'))
    # tiger
    chessArrA.append(jc.Chess(6, 0, 5, 'A', 'T'))
    chessArrB.append(jc.Chess(0, 8, 5, 'B', 'T'))
    # lion
    chessArrA.append(jc.Chess(0, 0, 6, 'A', 'I'))
    chessArrB.append(jc.Chess(6, 8, 6, 'B', 'I'))
    # elephant
    chessArrA.append(jc.Chess(6, 2, 7, 'A', 'E'))
    chessArrB.append(jc.Chess(0, 6, 7, 'B', 'E'))

    global chessA, chessB, gameEnd, turn
    chessA = 8
    chessB = 8
    gameEnd = False
    turn = 'A'

    view.printBoard(chessArrA, chessArrB, den, trap, river)
    view.remind()


def getChess(chessName):  # get chess obj by chess name
    for i in range(8):
        if chessArrA[i].isName(chessName):
            return chessArrA[i]
        elif chessArrB[i].isName(chessName):
            return chessArrB[i]


def getChessByPos(x, y):  # get chess obj by position
    for i in range(8):
        if chessArrA[i].inPos(x, y):
            return chessArrA[i]
        elif chessArrB[i].inPos(x, y):
            return chessArrB[i]


def haveChess(x, y):  # check a specific position have chess or not
    for i in range(8):
        if chessArrA[i].inPos(x, y):
            return True
        elif chessArrB[i].inPos(x, y):
            return True
    return False


def capture(movingChess, capChess):  # chess capturing
    # movingChess is the chess that are moving in current turn
    # capChess is the chess that to be capture
    global chessA, chessB
    canCapture = False

    if capChess.getPlayer() == 'A':
        if trap.isTrapB(capChess.getX(), capChess.getY()):
            canCapture = True
    else:
        if trap.isTrapA(capChess.getX(), capChess.getY()):
            canCapture = True

    if river.isRiver(movingChess.getX(), movingChess.getY()):  # rat eat rat in river
        if river.isRiver(capChess.getX(), capChess.getY()):
            canCapture = True

    elif capChess.getRank() == 7:
        if movingChess.getRank() == 0:
            canCapture = True

    elif capChess.getRank() <= movingChess.getRank():
        canCapture = True

    if canCapture:
        movingChess.setPos(capChess.getX(), capChess.getY())
        capChess.setPos(-1, -1)
        if capChess.getPlayer() == 'A':
            chessA -= 1
        else:
            chessB -= 1
        return True

    return False


def canMove(chess, x, y):  # check chess can move to specific position or not
    xArr = {0, 1, 2, 3, 4, 5, 6}
    yArr = {0, 1, 2, 3, 4, 5, 6, 7, 8}

    if x not in xArr or y not in yArr:
        return False

    if chess.getPlayer() == 'A':
        if den.isDenA(x, y):
            return False
    else:
        if den.isDenB(x, y):
            return False

    if chess.getRank() == 0:
        if river.isRiver(chess.getX(), chess.getY()):
            if haveChess(x, y) and not river.isRiver(x, y):
                return False
    else:
        if river.isRiver(x, y):
            return False

    if haveChess(x, y):
        if getChessByPos(x, y).getPlayer() == chess.getPlayer():
            return False

    return True


def jump(chess, pos):  # jump over the river for lion and tiger
    canJump = True
    x = chess.getX()
    y = chess.getY()
    if pos == 'U':
        for i in range(3):
            if haveChess(x, y - (i + 1)):
                canJump = False
                break
            if i == 2:
                y -= 4
    elif pos == 'D':
        for i in range(3):
            if haveChess(x, y + (i + 1)):
                canJump = False
                break
            if i == 2:
                y += 4
    elif pos == 'L':
        for i in range(2):
            if haveChess(x - (i + 1), y):
                canJump = False
                break
            if i == 1:
                x -= 3
    else:
        for i in range(2):
            if haveChess(x + (i + 1), y):
                canJump = False
                break
            if i == 1:
                x += 3

    if canJump:
        if haveChess(x, y):
            if getChessByPos(x, y).getPlayer() != chess.getPlayer():
                if capture(chess, getChessByPos(x, y)):
                    return True
        else:
            chess.setPos(x, y)
            return True

    return False


def move(chess, pos):  # actual movement
    x = chess.getX()
    y = chess.getY()
    if pos == 'U':
        y -= 1
    elif pos == 'D':
        y += 1
    elif pos == 'L':
        x -= 1
    else:
        x += 1

    if canMove(chess, x, y):
        if haveChess(x, y):
            if capture(chess, getChessByPos(x, y)):
                return True
        else:
            chess.setPos(x, y)
            return True
    elif chess.getRank() == 5 or chess.getRank() == 6:
        if river.isRiver(x, y):
            if jump(chess, pos):
                return True

    return False


def chessMove(command):  # command --> actual movement
    chessName, pos = command.split(' ')
    global turn
    if chessName in {"AR", "BR", "AC", "BC", "AD", "BD", "AW", "BW", "AL", "BL", "AT", "BT", "AI", "BI", "AE", "BE"}:
        if pos in {'U', 'D', 'R', 'L'}:
            if chessName[0] == turn:
                if not move(getChess(chessName), pos):
                    view.errMessage(4)
                else:
                    view.printBoard(chessArrA, chessArrB, den, trap, river)
                    if turn == 'A':
                        turn = 'B'
                    else:
                        turn = 'A'
                    if not winCheck():
                        view.remind()
            else:
                view.errMessage(6)
        else:
            view.errMessage(3)
    else:
        view.errMessage(2)


def winCheck():  # check if there is a winner
    global gameEnd
    for i in range(8):
        if den.isDenB(chessArrA[i].getX(), chessArrA[i].getY()):
            gameEnd = True
            view.winMessage('A')
            return True
        elif den.isDenA(chessArrB[i].getX(), chessArrB[i].getY()):
            gameEnd = True
            view.winMessage('B')
            return True

    if chessB == 0:
        gameEnd = True
        view.winMessage('A')
        return True
    elif chessA == 0:
        gameEnd = True
        view.winMessage('B')
        return True

    return False


def commandTranslator(command):  # get command from controller --> do something
    if command == 'EXIT':
        exit()
    elif command == 'RESTART':
        init()
    elif len(command) == 4 and command[2] == " ":
        if not gameEnd:
            chessMove(command)
        else:
            view.errMessage(5)
    else:
        view.errMessage(1)
