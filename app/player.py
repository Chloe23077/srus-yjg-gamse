class Player:
    def __init__(self, uid: str, name: str) -> None:
        self._uid = uid
        self._name = name

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    def __str__(self):
        return f"Player(uid={self._uid}, name={self._name})"
