import threading
from typing import List

from game.dice import Dice
from game.game import SnakeAndLadderGame
from game.player import Player
from singleton import singleton


@singleton
class GameController:
    def __init__(self):
        self.game_id_to_game = {}

    def start_new_game(self, players: List[Player], dices: List[Dice], board_size: int):
        game = SnakeAndLadderGame(players=players, dices=dices, board_size=board_size)
        self.game_id_to_game[game.id] = game
        thread = threading.Thread(target=game.play_game)
        thread.start()
