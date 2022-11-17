import model as ml
import time
# init for no chess on board
def demo_init():
    ml.chessArrA.clear()
    ml.chessArrB.clear()
    # rat
    ml.chessArrA.append(ml.jc.Chess(-1, -1, 0, 'A', 'R'))
    ml.chessArrB.append(ml.jc.Chess(-1, -1, 0, 'B', 'R'))
    # cat
    ml.chessArrA.append(ml.jc.Chess(-1, -1, 1, 'A', 'C'))
    ml.chessArrB.append(ml.jc.Chess(-1, -1, 1, 'B', 'C'))
    # dog
    ml.chessArrA.append(ml.jc.Chess(-1, -1, 2, 'A', 'D'))
    ml.chessArrB.append(ml.jc.Chess(-1, -1, 2, 'B', 'D'))
    # wolf
    ml.chessArrA.append(ml.jc.Chess(-1, -1, 3, 'A', 'W'))
    ml.chessArrB.append(ml.jc.Chess(-1, -1, 3, 'B', 'W'))
    # leopard
    ml.chessArrA.append(ml.jc.Chess(-1, -1, 4, 'A', 'L'))
    ml.chessArrB.append(ml.jc.Chess(-1, -1, 4, 'B', 'L'))
    # tiger
    ml.chessArrA.append(ml.jc.Chess(-1, -1, 5, 'A', 'T'))
    ml.chessArrB.append(ml.jc.Chess(-1, -1, 5, 'B', 'T'))
    # lion
    ml.chessArrA.append(ml.jc.Chess(-1, -1, 6, 'A', 'I'))
    ml.chessArrB.append(ml.jc.Chess(-1, -1, 6, 'B', 'I'))
    # elephant
    ml.chessArrA.append(ml.jc.Chess(-1, -1, 7, 'A', 'E'))
    ml.chessArrB.append(ml.jc.Chess(-1, -1, 7, 'B', 'E'))

    ml.chessA = 8
    ml.chessB = 8
    ml.gameEnd = False
    ml.turn = 'A'

def demo_print():
    ml.view.printBoard(ml.chessArrA, ml.chessArrB, ml.den, ml.trap, ml.river)
    ml.view.remind()

def demo_enter():
    command = input()
    ml.commandTranslator(command.upper())

def demo_Move():
    ml.init()
    demo_enter() # 'AE D'
    demo_enter() # 'AE D' --> not allow
    demo_enter() # 'BW R'
    demo_enter() # 'AE L' --> cannot go river
    demo_enter() # 'aR r' --> show both upper case and lower case can enter

def demo_capture():
    demo_init()
    ml.chessArrA[1].setPos(5, 1)
    ml.chessArrA[5].setPos(0, 7)
    ml.chessArrB[0].setPos(4, 1)
    ml.chessArrB[5].setPos(6, 1)
    ml.turn = 'B'
    demo_print()
    demo_enter() #  'BR R' --> show lower rank cannot capture higher rank
    demo_enter() #  'BT L' --> higher rank can capture lower rank

def demo_river():
    demo_init()
    ml.chessArrA[0].setPos(0, 3)
    ml.chessArrA[1].setPos(0, 4)
    ml.chessArrB[0].setPos(2, 2)
    ml.chessArrB[5].setPos(0, 7)
    demo_print()
    demo_enter()  # 'AC R' -->
    demo_enter()  # 'AR R' -->
    demo_enter()  # 'BR L'
    demo_enter()  # 'AR U' --> cannot capture rat they are no both in river/ground
    demo_enter()  # 'AR D'
    demo_enter()  # 'BR D'
    demo_enter()  # 'AR U' --> rat capture rat in river

def demo_jump():
    demo_init()
    ml.chessArrA[0].setPos(0, 3)
    ml.chessArrA[6].setPos(0, 4)
    ml.chessArrB[5].setPos(3, 3)
    ml.chessArrB[0].setPos(4, 4)
    demo_print()
    demo_enter() # 'AI R' --> show lion jump over the river
    demo_enter() # 'BT L' --> show Tiger jump over the river with capturing
    demo_enter() # 'AI R' --> show lion cannot jump with blocking
    demo_enter() # 'AI L'

def demo_trap():
    demo_init()
    ml.chessArrB[6].setPos(3, 2)
    ml.chessArrA[0].setPos(4, 2)
    ml.chessArrA[6].setPos(2, 0)
    ml.chessArrB[0].setPos(1, 0)
    demo_print()
    demo_enter() # 'AR L' --> cannot capture
    demo_enter() # 'AR U'
    demo_enter() # 'BI U' --> to trap
    demo_enter() # 'AR L' --> can capture
    demo_enter() # 'BR R' --> only enemy trap active

def demo_winCondition1():
    demo_init()
    ml.chessArrA[0].setPos(3, 7)
    ml.chessArrB[0].setPos(5, 5)
    demo_print()
    demo_enter()  # 'AR D' --> win condition 1

def demo_winCondition2():
    demo_init()
    ml.chessA = 3
    ml.chessB = 1
    ml.chessArrA[0].setPos(2, 3)
    ml.chessArrA[1].setPos(3, 5)
    ml.chessArrA[7].setPos(3, 4)
    ml.chessArrB[5].setPos(3, 6)
    ml.turn = 'B'
    demo_print()
    demo_enter()  # 'BT U'
    demo_enter()  # 'AE D'

demo_Move()
time.sleep(2)

demo_capture()
time.sleep(2)

demo_river()
time.sleep(2)

demo_jump()
time.sleep(2)

demo_trap()
time.sleep(2)

demo_winCondition1()
time.sleep(2)

demo_winCondition2()
time.sleep(2)