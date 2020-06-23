from src.game.pieces import Piece, ABC, abstractmethod


# TODO: Think about if I really need to make a different implementation of make_move function for IA or Player...

class Player(ABC):

    def __init__(self, name: str, is_human: bool, team: str):
        self.name = name
        self.is_human = is_human
        self.team = team

    @abstractmethod
    def make_move(self, piece: Piece, move: str):
        pass


class Human(Player):

    def __init__(self, name: str, team: str):
        super().__init__(name=name, is_human=True, team=team)

    def make_move(self, piece: Piece, move: str):
        pass


class IA(Player):

    def __init__(self, name: str, team: str):
        super().__init__(name=name, is_human=False, team=team)

    def make_move(self, piece: Piece, move: str):
        pass
