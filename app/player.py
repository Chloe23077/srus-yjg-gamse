class Player:
    def __init__(self, uid: str, name: str) -> None:
        """
        Initializes a Player object with a unique id and a name.

        Args:
            uid (str): The unique identifier of the player.
            name (str): The name of the player.
        """
        self._uid = uid
        self._name = name

    @property
    def uid(self) -> str:
        """
        Returns the unique identifier of the player.

        Returns:
            str: The unique identifier of the player.
        """
        return self._uid

    @property
    def name(self) -> str:
        """
        Return the name of the player.

        Returns:
            str: The name of the player.
        """
        return self._name

    def __str__(self):
        """
        Returns a string representation of the player info.

        Returns:
            str: A string representing the player as "Player(uid=..., name=...)".
        """
        return f"Player(uid={self._uid}, name={self._name})"
