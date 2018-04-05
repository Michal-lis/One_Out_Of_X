import unittest
import gameflow

"""Tests yet to be written"""


class TestPlayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        # runs before evry test
        self.player1 = gameflow.Player('a', 1)
        self.player2 = gameflow.Player('b', 2)
        self.player3 = gameflow.Player('c', 3)

    def tearDown(self):
        # runs after every test
        pass

    def test_get_players(self):
        # important naming  to start with test_
        result = gameflow.get_players()
        self.assertEqual(result, [self.player1, self.player2, self.player3])


if __name__ == '__main__':
    unittest.main()
