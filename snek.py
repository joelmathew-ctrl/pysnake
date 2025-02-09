# Name: snek.py
# Author: Joel Mathew

import numpy as np 

class Snake:
    pass

class Apple:
    pass

class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def board_matrix(self):
        # Return a matrix filled with spaces
        return np.full((self.height, self.width), " ")

    def render(self):
        board = self.board_matrix()
        for y in range(self.height):
            print("".join(board[y]))  # Join elements of each row into a single string

game = Game(10, 20)
game.render()
