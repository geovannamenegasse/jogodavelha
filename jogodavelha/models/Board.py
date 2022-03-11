from jogodavelha.models.Position import Position

class Board():
  def __init__(self, dimension):
    self.dimension = dimension
    self.matrix = [[Position(dimension-(x+1), y) for x in range(dimension)] for y in range(dimension)]
  
  def makeTheMovementInBoard(self, x, y, player):
    self.matrix[self.dimension-(x+1)][y].setPlayerInPosition(player)
  
  def checkIfPlayerWon(self, player):
    if self.isPlayerDiagonalWinner(player) or self.isPlayerHorizontalWinner(player) or self.isPlayerVerticalWinner(player):
      return player
    return self.checkIfDrawWon()

  def isPlayerDiagonalWinner(self, player):
    return player == self.getCommonElementInSecDiagonal() or player == self.getCommonElementInPrimDiagonal()

  def isPlayerHorizontalWinner(self, player):
    for row in self.matrix:
      if player == self.getCommonElementInList(row):
        return True    
    return False
    
  def isPlayerVerticalWinner(self, player):
    for column in zip(*self.matrix):
      if player == self.getCommonElementInList(column):
        return True 
    return False

  def checkIfDrawWon(self):
    for row in self.matrix:
      for column in row:
        if not column.player:
          return None  
    return "Draw"

  def getCommonElementInList(self, list):
    first = list[0]
    for item in list:
      if first.player != item.player:
        return None
    return first.player

  def getCommonElementInSecDiagonal(self):
    first = self.matrix[0][0].player
    for row in range(self.dimension):
      for column in range(self.dimension):
        if row == column and self.matrix[row][column].player != first:        
          return None
    return first

  def getCommonElementInPrimDiagonal(self):
    first = self.matrix[0][self.dimension-1].player
    for row in range(self.dimension):
      for column in range(self.dimension):
        if row + column == self.dimension-1 and self.matrix[row][column].player != first:        
          return None
    return first