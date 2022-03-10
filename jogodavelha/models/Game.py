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
        if self.currentPlayer == 'X': 
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'

    # def toDict(self):
    #     return { "id" : str(self.id), "firstPlayer" : self.firstPlayer, "winner" : self.winner }