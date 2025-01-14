import time
import uuid
from typing import List

from game.board import Board
from game.dice import Dice, DiceManager
from game.player import Player


class SnakeAndLadderGame:
    def __init__(self, players: List[Player], dices: List[Dice], board_size: int):
        self.dice_manager = DiceManager(dices)
        self.players = players
        self.board = Board(board_size)
        self.board.add_snakes_and_ladders()
        self.dices = dices
        self.id = uuid.uuid4()
        self.board_size = board_size
        self.current_player_index = 0

    def is_game_over(self):
        return any(player.position == self.board_size for player in self.players)

    def play_game(self):
        while not self.is_game_over():
            current_player = self.players[self.current_player_index]
            dice_roll = self.dice_manager.roll_dices()
            new_position = current_player.position + dice_roll
            if new_position == self.board.board_size:
                print(f"{str(self.id)} is won by {current_player.name} wins!!!")
                return
            elif new_position <= self.board.board_size:
                new_position = self.board.get_next_position(new_position)
                print(
                    f"{str(self.id)} status => {current_player.name} moved from {current_player.position} to {new_position}"
                )
                current_player.position = self.board.get_next_position(new_position)
            self.current_player_index = (self.current_player_index + 1) % len(
                self.players
            )
            time.sleep(0.1)
