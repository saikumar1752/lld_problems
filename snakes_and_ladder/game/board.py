import random
from typing import Dict

from game.ladder import Ladder
from game.snake import Snake


class Board:
    def __init__(self, board_size: int):
        self.board_size = board_size
        self.from_to_snake: Dict[int, int] = {}
        self.from_to_ladder: Dict[int, int] = {}

    def add_snakes_and_ladders(self):
        # 10 percent of cells will have ladders.
        for _ in range(self.board_size // 10):
            while True:
                start = random.randint(1, self.board_size - 1)
                end = random.randint(start + 1, self.board_size)
                if end < self.board_size:
                    try:
                        self.add_ladder(Ladder(start, end))
                    except Exception:
                        continue
                    break

        # 10 percent of cells with have snakes.
        for _ in range(self.board_size // 10):
            while True:
                end = random.randint(1, self.board_size - 1)
                start = random.randint(end + 1, self.board_size)
                if start < self.board_size:
                    try:
                        self.add_snake(Snake(start, end))
                    except Exception:
                        continue
                    break

    def add_snake(self, snake: Snake):
        if snake.from_cell in self.from_to_snake:
            raise Exception("Snake already added to board at this position")
        if snake.from_cell in self.from_to_ladder:
            raise Exception("Ladder already added to board at this position")
        self.from_to_ladder[snake.from_cell] = snake.to_cell

    def add_ladder(self, ladder: Ladder):
        if ladder.from_cell in self.from_to_snake:
            raise Exception("Snake already added to board at this position")
        if ladder.from_cell in self.from_to_ladder:
            raise Exception("Ladder already added to board at this position")
        self.from_to_ladder[ladder.from_cell] = ladder.to_cell

    def get_next_position(self, current_position: int):
        if current_position in self.from_to_snake:
            return self.from_to_snake[current_position]
        if current_position in self.from_to_ladder:
            return self.from_to_ladder[current_position]
        return current_position
