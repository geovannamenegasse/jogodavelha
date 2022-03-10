
class GameHistory():
    
    def __init__(self):
        self.games = []
        # self.history = []

    def addGame(self, game):
        self.games.append(game)
        # self.history.append(game.toDict())

    def getGameById(self, id):
        currentGame = None
        for game in self.games:
            if str(game.id) == id: 
                currentGame = game
                break
        return currentGame

    # def getHistory(self):
    #     return self.history