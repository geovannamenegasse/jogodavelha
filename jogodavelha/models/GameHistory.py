class GameHistory():
    
    def __init__(self):
        self.games = []

    def addGame(self, game):
        self.games.append(game)

    def getGameById(self, id):
        currentGame = None
        for game in self.games:
            if str(game.id) == id: 
                currentGame = game
                break
        return currentGame