from player import Player
from player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, player: Player):
        if self._root is None:
            self._root = PlayerBNode(player)
        else:
            self._insert_recursive(self._root, player)

    def _insert_recursive(self, current: PlayerBNode, player:Player):
        if player.name < current.player.name:
            if current.left is None:
                current.left = PlayerBNode(player)
            else:
                self._insert_recursive(current.left, player)
        elif player.name > current.player.name:
            if current.right is None:
                current.right = PlayerBNode(player)
            else:
                self._insert_recursive(current.right, player)
        else:
            current.player = player


def main():
    player1 = Player("1", "Chloe",100)
    player2 = Player("2", "John",200)
    player3 = Player("3", "Bob",120)

    player_bst = PlayerBST()

    player_bst.insert(player1)
    player_bst.insert(player2)
    player_bst.insert(player3)

    print("Root: ", player_bst.root.player)
    print("Left Child: ", player_bst.root.left.player)
    print("Right Child: ", player_bst.root.right.player)


if __name__ == "__main__":
    main()
