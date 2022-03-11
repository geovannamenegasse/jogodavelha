from jogodavelha.models.Position import Position

class Board():
  def __init__(self, dimension):
    self.dimension = dimension
    self.matrix = [[Position(dimension-(x+1), y) for x in range(dimension)] for y in range(dimension)]
  
  def makeTheMovementInBoard(self, x, y, player):
    self.matrix[self.dimension-(x+1)][y].setPlayerInPosition(player)
  
  def checkWinner(self):
    winner = self.checkWinnerDiagonals()  
    if winner:
      return winner    
    winner = self.checkWinnerLines()
    if winner:
      return winner    
    winner = self.checkWinnerColumns()
    if winner:
      return winner
    return self.checkEmptyPositions()

  def checkWinnerDiagonals(self):
    if self.matrix[0][0].player == self.matrix[1][1].player == self.matrix[2][2].player:
      return self.matrix[0][0].player
    if self.matrix[2][0].player == self.matrix[1][1].player == self.matrix[0][2].player:
      return self.matrix[2][0].player
    return None

  def checkWinnerLines(self):
    for row in range(self.dimension):
      if self.matrix[row][0].player == self.matrix[row][1].player == self.matrix[row][2].player:
        return self.matrix[row][0].player    
    return None
    
  def checkWinnerColumns(self):
    for column in range(self.dimension):
      if self.matrix[0][column].player == self.matrix[1][column].player == self.matrix[2][column].player:
        return self.matrix[0][column].player 
    return None

  def checkEmptyPositions(self):
    for row in range(self.dimension):
      for column in range(self.dimension):
        if self.matrix[row][column].player == None:
          return None  
    return "Draw"
