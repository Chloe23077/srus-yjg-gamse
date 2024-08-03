# This is the implementation of double linked list
from player import Player
from player_node import PlayerNode


class PlayerList:
    def __init__(self) -> None:
        self._head = None

    def is_empty(self):
        return self._head is None

    def insert_first(self, player: Player):
        new_node = PlayerNode(player)

        if self.is_empty():
            self._head = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

    def __str__(self):
        node = []
        current = self._head
        while current is not None:
            node.append(str(current))
            current = current.next
        return " -> ".join(node)


# step 5 commit 전 여기 node부터 다시하기 __str__여기부터.