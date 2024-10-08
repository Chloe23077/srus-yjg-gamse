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

    def search(self, name: str) -> PlayerBNode:
        return self._search_recursive(self._root, name)

    def _search_recursive(self, current: PlayerBNode, name: str):
        if current is None:
            return None
        if name == current.player.name:
            return current
        elif name < current.player.name:
            return self._search_recursive(current.left, name)
        else:
            return self._search_recursive(current.right, name)

    def new_sorted_list(self):
        sorted_list = []
        self._in_order(self._root, sorted_list)
        return sorted_list

    def _in_order(self, node: PlayerBNode, sorted_list: list):
        if node is not None:
            self._in_order(node.left, sorted_list)
            sorted_list.append(node.player)
            self._in_order(node.right, sorted_list)

    def balanced_bst(self):
        sorted_list = self.new_sorted_list()
        return self._balanced_bst_recursive(sorted_list)

    def _balanced_bst_recursive(self, sorted_list: list):
        if not sorted_list:
            return None

        mid_index = len(sorted_list) // 2
        mid_node = PlayerBNode(sorted_list[mid_index])

        mid_node.left = self._balanced_bst_recursive(sorted_list[:mid_index])
        mid_node.right = self._balanced_bst_recursive(sorted_list[mid_index + 1:])

        return mid_node


def main():
    player1 = Player("1", "Chloe",100)
    player2 = Player("2", "John",200)
    player3 = Player("3", "Bob",120)
    player4 = Player("4", "Jack",120)
    player5 = Player("5", "Oliver",120)
    player6 = Player("6", "William",120)

    player_bst = PlayerBST()

    player_bst.insert(player1)
    player_bst.insert(player2)
    player_bst.insert(player3)
    player_bst.insert(player4)
    player_bst.insert(player5)
    player_bst.insert(player6)

    # print("Root: ", player_bst.root.player)
    # print("Left Child: ", player_bst.root.left.player)
    # print("Right Child: ", player_bst.root.right.player)

    # target_name = "John"
    # found_node = player_bst.search(target_name)

    # if found_node:
    #     print(f"Player found: {found_node.player}")

    print("unbalanced BST: ")
    print("Root: ", player_bst.root.player)

    balanced_bst_root = player_bst.balanced_bst()
    print("balance BST: ", balanced_bst_root.player)


if __name__ == "__main__":
    main()
