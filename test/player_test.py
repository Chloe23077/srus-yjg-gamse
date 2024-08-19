# this script is testing the player.py
import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        # create an instance of Player class
        self.player1 = Player(uid="1", name="Chloe", score=120)
        self.player2 = Player(uid="2", name="Alice", score=200)
        self.player3 = Player(uid="3", name="John", score=120)
        self.player4 = Player(uid="4", name="J", score=160)

    def test_initialization(self):
        self.assertEqual(self.player1.uid, "1")
        self.assertEqual(self.player1.name, "Chloe")
        self.assertEqual(self.player1.score, 120)

    def test_uid_property(self):
        self.assertEqual(self.player1.uid, "1")

    def test_name_property(self):
        self.assertEqual(self.player1.name, "Chloe")

    def test_str_method(self):
        # testing the class value in string format
        self.assertEqual(str(self.player1), "Player(uid=1, name=Chloe, score=120)")

    def test_add_password(self):
        self.player1.add_password("password1234")
        self.assertIsNotNone(self.player1._hash_password)

    def test_verify_password(self):
        self.player1.add_password("password1234")
        self.assertTrue(self.player1.verify_password("password1234"))
        self.assertFalse(self.player1.verify_password("Password123"))

    def test_score_property(self):
        self.assertEqual(self.player1.score, 120)

    def test_eq_method(self):
        self.assertTrue(self.player1.__eq__(self.player3))
        self.assertFalse(self.player1.__eq__(self.player2))

    def test_ge_method(self):
        self.assertFalse(self.player1.__ge__(self.player2))

    def test_sort_player(self):
        players = [self.player1, self.player2, self.player3, self.player4]
        sorted_players = Player.sort_player(players)
        self.assertEqual(sorted_players[0].score, 200)
        self.assertEqual(sorted_players[1].score, 160)
        self.assertEqual(sorted_players[2].score, 120)
        self.assertEqual(sorted_players[3].score, 120)


if __name__ == '__main__':
    unittest.main()

