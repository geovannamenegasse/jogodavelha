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

  xCoordRead = request.form["x"]
  yCoordRead = request.form["y"]
  playerRead = request.form["player"]

  currentGame = gameHistory.getGameById(id)
  if not currentGame:
    return { "msg" : "Partida não encontrada" }

  if not currentGame.checkCurrentPlayerTurn(playerRead):
    return { "msg" : "Não é turno do jogador" }

  currentGame.board.makeTheMovementInBoard(xCoordRead, yCoordRead, playerRead)
  # print(currentGame.board)
  
  winner = currentGame.board.checkWinner()
  if winner:
    return { "msg" : "Partida finalizada", "winner" : winner }

  currentGame.changeTheCurrentPlayer()

  return Response(status = 200)


# @app.route("/games", methods = ['GET'])
# def games():   
#     return json.dumps(gameHistory.getHistory())
