from flask import request, Response
from jogodavelha import app, gameHistory
from jogodavelha.models.Game import Game

@app.route("/game", methods = ['POST'])
def game(): 
  newGame = Game()
  gameHistory.addGame(newGame)  
  return { "id" : newGame.id, "firstPlayer" : newGame.firstPlayer }

@app.route("/game/<string:id>/movement", methods = ['POST'])
def movement(id):
  xCoordinateRead = request.json["position"]["x"]
  yCoordinateRead = request.json["position"]["y"]
  playerRead = request.json["player"]

  currentGame = gameHistory.getGameById(id)
  if not currentGame:
    return { "msg" : "Partida não encontrada" }
  
  if currentGame.winner:
    return { "msg" : "Partida finalizada", "winner" : currentGame.winner } 

  if not currentGame.checkCurrentPlayerTurn(playerRead):
    return { "msg" : "Não é turno do jogador" }
  
  currentGame.board.makeTheMovementInBoard(xCoordinateRead, yCoordinateRead, playerRead)
  currentGame.winner = currentGame.board.checkIfPlayerWon(currentGame.currentPlayer)

  if currentGame.winner:
    return { ("status" if currentGame.winner == "Draw" else "msg") : "Partida finalizada", "winner" : currentGame.winner }

  currentGame.changeTheCurrentPlayer()
  return Response(status = 200)
  
