class GameHistory():  
  def __init__(self):
    self.games = []

  def addGame(self, game):
    self.games.append(game)

  def getGameById(self, id):
    for game in self.games:
      if game.id == id: 
        return game
    return None