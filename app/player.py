from argon2 import PasswordHasher

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
        self._hash_password= None

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

    def __str__(self):
        """
        Returns a string representation of the player info.

        Returns:
            str: A string representing the player as "Player(uid=..., name=...)".
        """
        return f"Player(uid={self._uid}, name={self._name})"
