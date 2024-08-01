from player import Player


class PlayerNode:
    def __init__(self, player: Player) -> None:
        self._player = player
        self._next = None
        self._prev = None

    @property
    def player(self) -> Player:
        return self._player

    # This sets the property and setter for next
    @property
    def next(self) -> Player:
        return self._next

    @next.setter
    def next(self, next_node: Player):
        self._next = next_node

    # This sets the property and setter for prev
    @property
    def prev(self) -> Player:
        return self._prev

    @prev.setter
    def prev(self, prev_node: Player):
        self._prev = prev_node

    # creating a new property variable, called key
    def key(self):
        return self._player.uid

    def __str__(self):
        return f"PlayerNode(player={self._player}, next={self._next}, previous={self._prev})"
