import unittest
from AdvanceGUIandModularMathematics import result

class Test_Game(unittest.TestCase):

    def setUp(self):
        self.pl = "Player lost"
        self.pw = "Player won"
        self.d = "Draw"

    def test_result_player_lost(self):
        self.assertEqual(result(0,1), self.pl)
        self.assertEqual(result(1,2), self.pl)
        self.assertEqual(result(2,3), self.pl)
        self.assertEqual(result(3,4), self.pl)
        self.assertEqual(result(4,0), self.pl)
        self.assertEqual(result(4,1), self.pl)        

    def test_result_draw(self):
        self.assertEqual(result(1,1), self.d)
        self.assertEqual(result(2,2), self.d)
        self.assertEqual(result(3,3), self.d)
        self.assertEqual(result(4,4), self.d)
        self.assertEqual(result(0,0), self.d)

    def test_result_player_won(self):
        self.assertEqual(result(1,0), self.pw)
        self.assertEqual(result(2,1), self.pw)
        self.assertEqual(result(3,2), self.pw)
        self.assertEqual(result(4,3), self.pw)
        self.assertEqual(result(0,4), self.pw)
        self.assertEqual(result(0,3), self.pw)
    
if __name__ == '__main__':
    unittest.main(exit = False)
