import random, uuid
from jogodavelha.constants.constants import players, boardDimension
from jogodavelha.models.Board import Board

class Game():

    def __init__(self):
        self.id            = uuid.uuid4()
        self.firstPlayer   = random.choice(players)
        self.currentPlayer = self.firstPlayer
        self.winner        = None
        self.board         = Board(boardDimension)

    def checkCurrentPlayerTurn(self, player):
        return self.currentPlayer == player

    def changeTheCurrentPlayer(self):
        self.currentPlayer = players[1] if self.currentPlayer == players[0] else players[0]