from argon2 import PasswordHasher

class Player:
    def __init__(self, uid: str, name: str, score: int) -> None:
        """
        Initializes a Player object with a unique id and a name.

        Args:
            uid (str): The unique identifier of the player.
            name (str): The name of the player.
        """
        self._uid = uid
        self._name = name
        self._hash_password = None
        self._score = score

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

    def add_password(self, password: str) -> None:
        """
        Hashing the provided password and stores the hashed password using argon2.

        Args:
            password (str): The plaintext password to hash.
        """
        ph = PasswordHasher()
        self._hash_password = ph.hash(password)

    def verify_password(self, password: str) -> bool:
        """
        Verified that the provided password matches the stored hashed password.

        Args:
            password (str): The plaintext password to verify.

        Returns:
            bool: Ture if the password matches, False otherwise.
        """
        ph = PasswordHasher()
        try:
            return ph.verify(self._hash_password, password)
        except:
            return False

    @property
    def score(self) -> int:
        """
        Returns the score of the player.

        Returns:
             int: The score of the player.
        """
        return self._score

    @score.setter
    def score(self, new_score: int):
        """
        Sets a new score for the player.

        Args:
            new_score (int): The new score to set.
        """
        self._score = new_score

    def __eq__(self, other) -> bool:
        """
        Checks if the score of this player is equal to another player.

        Args:
            other (Player): The other player to compare with.

        Returns:
            bool: True if the scores are equal, False otherwise.
        """
        if isinstance(other, Player):
            return self._score == other._score
        return False

    def __ge__(self, other) -> bool:
        """
        Checks if the score of this player is greater than or equal  to another player.

        Args:
            other (Player): The other player to compare with.

        Returns:
            bool: True if the score is greater than or equal to, False otherwise.
        """
        if isinstance(other, Player):
            return self._score >= other._score
        return False
    @staticmethod
    def sort_player(players):
        """
        Sorts a list of Player in descending order on their scores using selection sort.

        Args:
            players (list of Player): The list of Player to sort.

        Returns:
            list of Player: The sorted list of Player.
        """
        for i in range(len(players)):
            max_index = i
            for j in range(i+1, len(players)):
                if players[j].score > players[max_index].score:
                    max_index = j
            temp = players[i]
            players[i] = players[max_index]
            players[max_index] = temp
        return players

    def __str__(self):
        """
        Returns a string representation of the player info.

        Returns:
            str: A string representing the player as "Player(uid=..., name=..., score=...)".
        """
        return f"Player(uid={self._uid}, name={self._name}, score={self._score})"
