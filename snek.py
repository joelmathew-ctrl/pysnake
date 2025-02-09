# Name: snek.py
# Author: Joel Mathew

import numpy as np 

class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, position):
        self.body = self.body[1:] + [position]

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]

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
