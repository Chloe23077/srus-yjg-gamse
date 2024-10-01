import unittest
from player import Player
from player_bnode import PlayerBNode
from player_bst import PlayerBST


class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        self.bst = PlayerBST()
        self.player1 = Player("1", "Chloe", 100)
        self.player2 = Player("2", "John", 200)
        self.player3 = Player("3", "Bob", 120)

        self.player_bst = PlayerBST()
        self.player_bst.insert(self.player1)
        self.player_bst.insert(self.player2)
        self.player_bst.insert(self.player3)

    def test_insert_first_node(self):
        self.bst.insert(self.player1)
        self.assertIsNotNone(self.bst.root)
        self.assertEqual(self.bst.root.player.name, "Chloe")

    def test_insert_update_existing_node(self):
        self.bst.insert(self.player1)
        self.bst.insert(self.player2)
        self.assertIsNotNone(self.bst.root.right)
        self.assertEqual(self.bst.root.right.player.name, "John")

    def test_search_existing_player(self):
        target = self.player_bst.search("John")
        self.assertIsNotNone(target)
        self.assertEqual(target.player.name, "John")


