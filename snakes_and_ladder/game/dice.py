import random
from typing import List


class Dice:
    def __init__(self, faces: int):
        self.faces = faces


class DiceManager:
    def __init__(self, dices: List[Dice]):
        self.dices = dices

    def roll_dices(self) -> int:
        return sum(random.randint(1, dice.faces) for dice in self.dices)
