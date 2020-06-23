from abc import ABC, abstractmethod


# TODO: Implement move/authorizec_move methods for every pieces
#  and add Board implementation + import

class Piece(ABC):

    def __init__(self, name: str, team: str, value: int):
        self.name = name
        self.team = team
        self.value = value
        self.kills = 0

    @abstractmethod
    def move(self, to_x: int, to_y: int, board: Board):
        pass

    @abstractmethod
    def authorized_moves(self, to_x: int, to_y: int, board: Board):
        pass


class Pawn(Piece):

    def __init__(self, team: str):
        super().__init__(name='p', team=team, value=1)

    def move(self, to_x: int, to_y: int, board: Board):
        pass

    def authorized_moves(self, to_x: int, to_y: int, board: Board):
        pass


class Rook(Piece):

    def __init__(self, team: str):
        super().__init__(name='R', team=team, value=5)

    def move(self, to_x: int, to_y: int, board: Board):
        pass

    def authorized_moves(self, to_x: int, to_y: int, board: Board):
        pass


class Bishop(Piece):

    def __init__(self, team: str):
        super().__init__(name='B', team=team, value=3)

    def move(self, to_x: int, to_y: int, board: Board):
        pass

    def authorized_moves(self, to_x: int, to_y: int, board: Board):
        pass


class Knight(Piece):

    def __init__(self, team: str):
        super().__init__(name='N', team=team, value=3)

    def move(self, to_x: int, to_y: int, board: Board):
        pass

    def authorized_moves(self, to_x: int, to_y: int, board: Board):
        pass


class Queen(Piece):

    def __init__(self, team: str):
        super().__init__(name='Q', team=team, value=9)

    def move(self, to_x: int, to_y: int, board: Board):
        pass

    def authorized_moves(self, to_x: int, to_y: int, board: Board):
        pass


class King(Piece):

    def __init__(self, team: str):
        super().__init__(name='K', team=team, value=999)

    def move(self, to_x: int, to_y: int, board: Board):
        pass

    def authorized_moves(self, to_x: int, to_y: int, board: Board):
        pass
