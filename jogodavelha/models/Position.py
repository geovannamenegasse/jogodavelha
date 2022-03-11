class Position():   
  def __init__(self, x, y):
    self.xCoordinate = x
    self.yCoordinate = y
    self.player      = None
  
  def setPlayerInPosition(self, player):
    self.player = player