import unittest
from jogodavelha import app, gameHistory
from jogodavelha.models.Game import Game

class TestGame(unittest.TestCase):
  def setUp(self):
    self.game = Game()
    self.game.firstPlayer = 'X'
    self.game.currentPlayer = 'X'
    gameHistory.addGame(self.game)

  def testMakeAMovement(self):
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 0,"y": 1}})
    assert response.status_code == 200

  def testReturnDiagonalWinner(self):     
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 0,"y": 0}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "O","position": {"x": 1,"y": 0}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 1,"y": 1}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "O","position": {"x": 0,"y": 1}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 2,"y": 2}})
    assert b'{"msg":"Partida finalizada","winner":"X"}' in response.get_data()

  def testReturnLineWinner(self):        
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 0,"y": 1}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "O","position": {"x": 1,"y": 0}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 1,"y": 1}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "O","position": {"x": 2,"y": 2}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 2,"y": 1}})
    assert b'{"msg":"Partida finalizada","winner":"X"}' in response.get_data()

  def testReturnColumnWinner(self):     
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 2,"y": 2}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "O","position": {"x": 0,"y": 2}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 2,"y": 1}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "O","position": {"x": 1,"y": 1}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 2,"y": 0}})
    assert b'{"msg":"Partida finalizada","winner":"X"}' in response.get_data()

  def testReturnDraw(self):
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 0,"y": 2}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "O","position": {"x": 1,"y": 2}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 2,"y": 2}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "O","position": {"x": 1,"y": 1}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 0,"y": 1}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "O","position": {"x": 2,"y": 1}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 1,"y": 0}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "O","position": {"x": 0,"y": 0}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": "X","position": {"x": 2,"y": 0}})
    assert b'{"msg":"Partida finalizada","winner":"Draw"}' in response.get_data()

  def testReturnErrorTurn(self):      
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": self.game.firstPlayer,"position": {"x": 0,"y": 0}})
    response = app.test_client().post('/game/'+str(self.game.id)+'/movement', json = {"player": self.game.firstPlayer,"position": {"x": 1,"y": 1}})
    assert b'{"msg":"N\\u00e3o \\u00e9 turno do jogador"}' in response.get_data()
  
  def testReturnErrorGameNotFound(self):      
    response = app.test_client().post('/game/'+str(self.game.id)+"a"+'/movement', json = {"player": self.game.firstPlayer,"position": {"x": 0,"y": 0}})
    assert b'{"msg":"Partida n\\u00e3o encontrada"}' in response.get_data()