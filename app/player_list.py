# This is the implementation of double linked list
from player import Player
from player_node import PlayerNode


class PlayerList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None

    def insert_first(self, player: Player):
        new_node = PlayerNode(player)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

        if self._tail is None:
            self._tail = new_node

    @property
    def tail(self):
        return self._tail

    def __str__(self):
        node = []
        current = self._head
        while current is not None:
            node.append(str(current))
            current = current.next
        return " -> ".join(node)

    def insert_last(self, player: Player):
        new_node = PlayerNode(player)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node


