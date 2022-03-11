import unittest
from jogodavelha import app, gameHistory
from jogodavelha.constants.constants import players
from jogodavelha.models.Game import Game

class TestGame(unittest.TestCase):
  def setUp(self):
    self.game = Game()
    self.game.firstPlayer = players[0]
    self.game.currentPlayer = players[0]
    gameHistory.addGame(self.game)

  def testMakeAMovement(self):
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 0,"y": 1}})
    assert response.status_code == 200

  def testReturnPrimaryDiagonalWinner(self):     
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 0,"y": 0}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 1,"y": 0}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 1,"y": 1}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 0,"y": 1}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 2,"y": 2}})
    assert b'{"msg":"Partida finalizada","winner":"X"}' in response.get_data()

  def testReturnSecondaryDiagonalWinner(self):     
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 0,"y": 2}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 0,"y": 1}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 1,"y": 1}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 2,"y": 1}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 2,"y": 0}})
    assert b'{"msg":"Partida finalizada","winner":"X"}' in response.get_data()

  def testReturnHorizontalWinner(self):        
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 0,"y": 1}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 1,"y": 0}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 1,"y": 1}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 2,"y": 2}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 2,"y": 1}})
    assert b'{"msg":"Partida finalizada","winner":"X"}' in response.get_data()

  def testReturnVerticalWinner(self):     
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 2,"y": 2}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 0,"y": 2}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 2,"y": 1}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 1,"y": 1}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 2,"y": 0}})
    assert b'{"msg":"Partida finalizada","winner":"X"}' in response.get_data()

  def testReturnDrawWon(self):
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 0,"y": 2}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 1,"y": 2}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 2,"y": 2}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 1,"y": 1}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 0,"y": 1}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 2,"y": 1}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 1,"y": 0}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 0,"y": 0}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 2,"y": 0}})
    assert b'{"status":"Partida finalizada","winner":"Draw"}' in response.get_data()

  def testReturnNotYourTurnError(self):      
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.firstPlayer,"position": {"x": 0,"y": 0}})
    response = app.test_client().post('/game/'+self.game.id+'/movement', json = {"player": self.game.firstPlayer,"position": {"x": 1,"y": 1}})
    assert b'{"msg":"N\\u00e3o \\u00e9 turno do jogador"}' in response.get_data()
  
  def testReturnGameNotFoundError(self):      
    response = app.test_client().post('/game/'+self.game.id+"a"+'/movement', json = {"player": self.game.currentPlayer,"position": {"x": 0,"y": 0}})
    assert b'{"msg":"Partida n\\u00e3o encontrada"}' in response.get_data()