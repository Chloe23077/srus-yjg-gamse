# This is the implementation of double linked list
from player import Player
from player_node import PlayerNode


class PlayerList:
    def __init__(self) -> None:
        """
        Initializes an empty double-linked list with head and tail pointers set to None.
        """
        self._head = None
        self._tail = None

    def is_empty(self) -> bool:
        """
        Check for double-linked list is empty.

        Return:
             bool: True if the list is empty, False otherwise.
        """
        return self._head is None

    def insert_first(self, player: Player):
        """
        Inserts a new player node at the head of the list.

        Args:
            player (Player): The player object to insert.
        """
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
        """
        Return the tail node of the list.

        Returns:
            The tail node in the list.
        """
        return self._tail

    def __str__(self):
        """
        Return a string representation of the double-linked list.

        Returns:
            str: A string representing the list, with node connected by '->'.
        """
        node = []
        current = self._head
        while current is not None:
            node.append(str(current))
            current = current.next
        return " -> ".join(node)

    def insert_last(self, player: Player):
        """
        Inserts a new player node at the end of the list.

        Args:
            player (Player): The player object to insert.
        """
        new_node = PlayerNode(player)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node

    # There is only one node in the list.
    def delete_first(self):
        """
        Delete the head node from the list.
        if the node is only one setting head and tail to None.
        else the node is more than two move on head to next.
        """
        if self.is_empty():
            return

        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None

    def delete_last(self):
        """
        Deletes the tail node from the list.
        if the node is only one setting head and tail to None.
        else the node is more than two move on tail to previous.
        :return:
        """
        if self.is_empty():
            return

        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None

    def delete_by_key(self, key: str):
        """
        Deletes a node from the list by key.

        Args:
            key (str): The key to identify the node to delete.

        Raises:
            ValueError If the key is not found in the list.
        """
        current = self._head

        while current is not None:
            if current.key == key:
                if current == self._head:
                    self.delete_first()
                elif current == self._tail:
                    self.delete_last()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
        raise ValueError("key not found!!!")

    def display(self, forward=True):
        """
        Displays the list nodes in forward of backward order.

        Args:
            forward (bool): True, display from head to tail. False, from tail to head.
        """
        if forward:
            current = self._head
            while current:
                print(current)
                current = current.next
        else:
            current = self._tail
            while current:
                print(current)
                current = current.prev




