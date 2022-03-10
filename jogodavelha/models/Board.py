from jogodavelha.models.Position import Position

class Board():

    def __init__(self, dimension):
      self.dimension = dimension
      self.board     = [[Position(dimension-(x+1), y) for x in range(dimension)] for y in range(dimension)]
    
    def makeTheMovementInBoard(self, x, y, player):
      self.board[self.dimension-(x+1)][y].setPlayerInPosition(player)
     
    def checkWinner(self):
      if self.board[0][0].player == self.board[1][1].player == self.board[2][2].player:
        return self.board[0][0].player
      
      if self.board[2][0].player == self.board[1][1].player == self.board[0][2].player:
        return self.board[2][0].player

      for row in range(self.dimension):
        if self.board[row][0].player == self.board[row][1].player == self.board[row][2].player:
          return self.board[row][0].player
      
      for column in range(self.dimension):
        if self.board[0][column].player == self.board[1][column].player == self.board[2][column].player:
          return self.board[0][column].player
      
      for row in range(self.dimension):
        for column in range(self.dimension):
          if self.board[row][column].player == None:
            return None        
      return "Draw"