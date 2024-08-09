from player import Player


class PlayerNode:
    def __init__(self, player: Player) -> None:
        """
        Initializes a new node for a player in the double-linked list.

        Args:
            player (Player): The player object to be stored.
        """
        self._player = player
        self._next = None
        self._prev = None

    @property
    def player(self) -> Player:
        """
        Retrieves the player object stored in this node.

        Returns:
             Player: The player object.
        """
        return self._player

    @property
    def next(self) -> Player:
        """
        Retrieves the next node in the list.

        Returns:
            The next node in the list.
        """
        return self._next

    @next.setter
    def next(self, next_node: Player):
        """
        Sets the property and setter for next.

        Args:
            next_node (Player): The node to be set as the next node.
        """
        self._next = next_node

    @property
    def prev(self) -> Player:
        """
        Retrieves the previous node in the list.

        Returns:
            The prev node in the list.
        """
        return self._prev

    @prev.setter
    def prev(self, prev_node: Player):
        """
        Sets the property and setter for prev.

        Args:
            prev_node (Player): The node to be set as the prev node.
        """
        self._prev = prev_node

    # creating a new property variable, called key
    @property
    def key(self):
        """
        Retrieves the unique key of the player stored in this node.

        Returns:
             The uid fo the player.
        """
        return self._player.uid

    def __str__(self):
        """
        Return a string representation of the PlayerNode.

        Returns:
             str: A string showing the player's info with next and prev node.
        """
        next_key = self._next.key if self._next else "None"
        prev_key = self._prev.key if self._prev else "None"
        return f"PlayerNode(player={self._player}, next={next_key}, previous={prev_key})"
