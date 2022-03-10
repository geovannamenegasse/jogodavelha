class Position():
    
    def __init__(self, x, y):
        self.xCoordinate = x
        self.yCoordinate = y
        self.player      = None
    
    def setPlayerInPosition(self, player):
        self.player = player

class Board():

    def __init__(self, dimension):
      self.dimension = dimension
      self.board     = [[Position(str(dimension-(x+1)), str(y)) for x in range(dimension)] for y in range(dimension)]

    def makeTheMovementInBoard(self, x, y, player):
        self.board[self.dimension-(int(x)+1)][int(y)].setPlayerInPosition(player)
     
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




    # def __str__(self):
    #     return self.get_readable_matrix_string(self.board)

    # def get_readable_matrix_string(self, matrix):
    #     strings = []
    #     for row in range(0, len(self.board), 1):
    #         for column in range(0, len(self.board), 1):
    #             strings.append(str(self.board[row][column].player))
    #     return "\n".join(strings)


  #  def updatePosition(self, x, y, player):
  #   #   for row in range(self.dimension):
  #   #     for column in range(self.dimension):
  #   #       if self.board[row][column].xCoordinate == x and self.board[row][column].yCoordinate == y:
  #       self.board[self.dimension - (int(x) + 1)][int(y)].setPlayer(player)
  #           # break