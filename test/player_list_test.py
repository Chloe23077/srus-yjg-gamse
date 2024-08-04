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
        self.pl.insert_first(self.player2)
        self.assertFalse(self.pl.is_empty())
        self.assertEqual(str(self.pl), "PlayerNode(player=Player(uid=2, name=Alex), next=1, previous=None) -> "
                        "PlayerNode(player=Player(uid=1, name=Chloe), next=None, previous=2)")

    def test_tail_update(self):
        self.pl.insert_first(self.player1)
        self.pl.insert_first(self.player2)
        self.assertEqual(self.pl.tail.player, self.player1)
        self.assertEqual(self.pl.tail.next, None)
        self.assertEqual(self.pl.tail.prev.player, self.player2)

    def test_insert_last(self):
        self.pl.insert_last(self.player1)
        self.pl.insert_last(self.player2)
        self.assertFalse(self.pl.is_empty())
        self.assertEqual(str(self.pl), "PlayerNode(player=Player(uid=1, name=Chloe), next=2, previous=None) -> "
                        "PlayerNode(player=Player(uid=2, name=Alex), next=None, previous=1)")

if __name__ == '__main__':
    unittest.main()