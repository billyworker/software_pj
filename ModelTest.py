import unittest
import model as ml


class ChessTestCase(unittest.TestCase):
    # initialization before the test
    @classmethod
    def setUpClass(cls):
        # jc as jungleClass in model
        cls.chess = ml.jc.Chess(0, 2, 0, 'A', 'R')

    # kill obj after all test finish in this class
    @classmethod
    def tearDownClass(cls):
        del cls.chess

    # test the Cheese can get the coordinate X =0
    def test_chess_getX(self):
        self.assertEqual(self.__class__.chess.getX(), 0)

    # test the Cheese can get the coordinate Y =2
    def test_chess_getY(self):
        self.assertEqual(self.__class__.chess.getY(), 2)

    # test the Cheese can get the rank where rat is rank 0
    def test_chess_getRank(self):
        self.assertEqual(self.__class__.chess.getRank(), 0)

    # test the Cheese can get the player belonging where should be player A
    def test_chess_getPlayer(self):
        self.assertIs(self.__class__.chess.getPlayer(), "A")

    # test the Cheese can get the name where  AR
    def test_chess_getName(self):
        self.assertMultiLineEqual(self.__class__.chess.getName(), "AR")

    # test the chess can change the position
    def test_chess_setPos(self):
        self.__class__.chess.setPos(1, 2)
        self.assertEqual(self.__class__.chess.getX(), 1)
        self.assertEqual(self.__class__.chess.getY(), 2)

    # test the can we check the chess position after change the position
    def test_chess_inPos(self):
        self.__class__.chess.setPos(1, 2)
        self.assertEqual(self.__class__.chess.inPos(1, 2), True)

    # test the can we check the name of chess
    def test_chess_isName(self):
        self.assertEqual(self.__class__.chess.isName('AR'), True)
        self.assertEqual(self.__class__.chess.isName('XX'), False)


class DenTestCase(unittest.TestCase):
    # test the Den function return
    def test_Den_isDen1(self):
        self.assertEqual(ml.den.isDen(3, 0), True)

    def test_Den_isDen2(self):
        self.assertEqual(ml.den.isDen(3, 8), True)

    def test_Den_isDenA(self):
        self.assertEqual(ml.den.isDenA(3, 0), True)

    def test_Den_isDenB(self):
        self.assertEqual(ml.den.isDenB(3, 8), True)


class TrapTestCase(unittest.TestCase):
    # test the Trap function return
    def test_Trap_isTrap(self):
        self.assertEqual(ml.trap.isTrap(2, 0), True)
        self.assertEqual(ml.trap.isTrap(4, 0), True)
        self.assertEqual(ml.trap.isTrap(3, 1), True)
        self.assertEqual(ml.trap.isTrap(2, 8), True)
        self.assertEqual(ml.trap.isTrap(4, 8), True)
        self.assertEqual(ml.trap.isTrap(3, 7), True)

    def test_Trap_isTrapA(self):
        self.assertEqual(ml.trap.isTrapA(2, 0), True)
        self.assertEqual(ml.trap.isTrapA(4, 0), True)
        self.assertEqual(ml.trap.isTrapA(3, 1), True)

    def test_Trap_isTrapB(self):
        self.assertEqual(ml.trap.isTrapB(2, 8), True)
        self.assertEqual(ml.trap.isTrapB(4, 8), True)
        self.assertEqual(ml.trap.isTrapB(3, 7), True)


class RiverTestCase(unittest.TestCase):
    # test the River function return
    def test_River_isRiver(self):
        self.assertEqual(ml.river.isRiver(1, 3), True)
        self.assertEqual(ml.river.isRiver(1, 4), True)
        self.assertEqual(ml.river.isRiver(1, 5), True)
        self.assertEqual(ml.river.isRiver(2, 3), True)
        self.assertEqual(ml.river.isRiver(2, 4), True)
        self.assertEqual(ml.river.isRiver(2, 5), True)
        self.assertEqual(ml.river.isRiver(4, 3), True)
        self.assertEqual(ml.river.isRiver(4, 4), True)
        self.assertEqual(ml.river.isRiver(4, 5), True)
        self.assertEqual(ml.river.isRiver(5, 3), True)
        self.assertEqual(ml.river.isRiver(5, 4), True)
        self.assertEqual(ml.river.isRiver(5, 5), True)


class ModelTestCase(unittest.TestCase):
    # before each test in this test, do initialization
    def setUp(self):
        ml.init()

    # test the chess in chessArray though name
    def test_model_getChess(self):
        self.assertIs(ml.getChess('AR'), ml.chessArrA[0])

    # test the chess in chessArray though position
    def test_model_getChessByPos(self):
        self.assertIs(ml.getChessByPos(5, 1), ml.chessArrA[1])

    # test there is it have chess
    def test_model_haveChess(self):
        self.assertEqual(ml.haveChess(0, 2), True)

    # test can capture the chess
    def test_model_capture(self):
        self.assertEqual(ml.capture(ml.chessArrB[7], ml.chessArrA[0]), True)  # elephant can capture rat
        self.assertEqual(ml.capture(ml.chessArrB[0], ml.chessArrA[7]), True)  # rat can capture elephant
        self.assertEqual(ml.capture(ml.chessArrB[0], ml.chessArrA[6]), False)  # rat can not capture lion
        ml.chessArrA[6].setPos(3, 7)
        self.assertEqual(ml.capture(ml.chessArrB[0], ml.chessArrA[6]), True)  # rat capture lion in den
        ml.init()
        # one rat in river and other rat is not in river ==> cannot capture
        ml.chessArrA[0].setPos(1, 3)
        ml.chessArrB[0].setPos(0, 3)
        self.assertEqual(ml.capture(ml.chessArrA[0], ml.chessArrB[0]), False)
        # both rat in river
        ml.chessArrA[0].setPos(1, 3)
        ml.chessArrB[0].setPos(2, 3)
        self.assertEqual(ml.capture(ml.chessArrA[0], ml.chessArrB[0]), True)

    # test chess can move to specific pos or not
    def test_model_canMove(self):
        self.assertEqual(ml.canMove(ml.chessArrA[0], 1, 2), True)  # rat can move to right one block
        self.assertEqual(ml.canMove(ml.chessArrA[4], 2, 3), False)  # Leopard cannot move to river
        self.assertEqual(ml.canMove(ml.chessArrB[0], 1, 4), True)  # rat can move to river
        self.assertEqual(ml.canMove(ml.chessArrA[0], 3, 0), False)  # team A cannot move to team A den
        self.assertEqual(ml.canMove(ml.chessArrA[0], 3, 8), True)  # team A can move to team B den

    # test chess can jump over river or not
    def test_model_jump(self):
        # test jumping from bottom to top
        ml.chessArrA[5].setPos(1, 6)
        self.assertEqual(ml.jump(ml.chessArrA[5], "U"), True)

        # rat block in river
        ml.chessArrA[0].setPos(1, 4)
        self.assertEqual(ml.jump(ml.chessArrA[5], "D"), False)

        # remove rat blocking
        ml.chessArrA[0].setPos(0, 2)
        self.assertEqual(ml.jump(ml.chessArrA[5], "D"), True)

        # test jumping from left to right
        ml.chessArrA[5].setPos(0, 3)
        self.assertEqual(ml.jump(ml.chessArrA[5], "R"), True)

        # rat block in river
        ml.chessArrA[0].setPos(1, 3)
        self.assertEqual(ml.jump(ml.chessArrA[5], "L"), False)

        # remove rat blocking
        ml.chessArrA[0].setPos(0, 2)
        self.assertEqual(ml.jump(ml.chessArrA[5], "L"), True)

    # test chess perform actual move
    def test_model_move(self):
        # move up
        self.assertEqual(ml.move(ml.chessArrA[0], "U"), True)
        self.assertEqual(ml.chessArrA[0].getY(), 1)
        # move down
        self.assertEqual(ml.move(ml.chessArrA[0], "D"), True)
        self.assertEqual(ml.chessArrA[0].getY(), 2)
        # move right
        self.assertEqual(ml.move(ml.chessArrA[0], "R"), True)
        self.assertEqual(ml.chessArrA[0].getX(), 1)
        # move left
        self.assertEqual(ml.move(ml.chessArrA[0], "L"), True)
        self.assertEqual(ml.chessArrA[0].getX(), 0)

    # check fulfill win requirement
    def test_model_winCheck(self):
        self.assertEqual(ml.winCheck(), False)
        # set a chess in team B in A's den
        ml.chessArrB[5].setPos(3, 0)
        self.assertEqual(ml.winCheck(), True)
        ml.init()
        # set all chess in team B are eaten
        ml.chessB = 0
        self.assertEqual(ml.winCheck(), True)


if __name__ == '__main__':
    unittest.main()
