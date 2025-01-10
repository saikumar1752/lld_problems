from game.dice import Dice
from game.player import Player
from game_controller import GameController

# Game 1
dices = [Dice(6), Dice(6)]
players = [
    Player(name="Player 1", id=1),
    Player(name="Player 2", id=2),
    Player(name="Player 3", id=3),
]
GameController().start_new_game(players, dices, 200)

# Game 2
dices = [Dice(6), Dice(6), Dice(6)]
players = [
    Player(name="Player 1", id=1),
    Player(name="Player 2", id=2),
    Player(name="Player 3", id=3),
]
GameController().start_new_game(players, dices, 300)
