import unittest
from player_list import PlayerList
from player import Player


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.pl = PlayerList()
        self.player1 = Player("1", "Chloe")
        self.player2 = Player("2", "Alex")

    def test_is_empty(self):
        self.assertTrue(self.pl.is_empty())

    def test_insert_first(self):
        self.pl.insert_first(self.player1)
        self.assertFalse(self.pl.is_empty())
        self.assertEqual(str(self.pl), f"PlayerNode(player={self.player1}, next=None, previous=None)")


if __name__ == '__main__':
    unittest.main()