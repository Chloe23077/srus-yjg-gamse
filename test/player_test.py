# this script is testing the player.py
import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        # create an instance of Player class
        self.player = Player(uid="1", name="Chloe")

    def test_initialization(self):
        self.assertEqual(self.player.uid, "1")
        self.assertEqual(self.player.name, "Chloe")

    def test_uid_property(self):
        self.assertEqual(self.player.uid, "1")

    def test_name_property(self):
        self.assertEqual(self.player.name, "Chloe")

    def test_str_method(self):
        # testing the class value in string format
        self.assertEqual(str(self.player), "Player(uid=1, name=Chloe)")


if __name__ == '__main__':
    unittest.main()

