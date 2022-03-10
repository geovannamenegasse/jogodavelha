from flask import Flask
from jogodavelha.models.GameHistory import GameHistory

app = Flask(__name__)
gameHistory = GameHistory()

from jogodavelha.controllers import game