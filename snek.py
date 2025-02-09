# Name: snek.py
# Author: Joel Mathew

import numpy as np 

# Defining directions 
UP = (0,1)
DOWN = (0,-1)
LEFT = (-1,0)
RIGHT = (1,0)

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
        self.snake = Snake([(1,1), (2,1), (3,1), (4,1)], UP)

    def board_matrix(self):
        # Return a matrix filled with spaces
        board = np.full((self.height, self.width), " ")
        for y in range(self.height):
            for x in range(self.width):
                board[0][x] = "-"
                board[y][0] = "|"
                board[self.height-1][x] = "-"
                board[y][self.width-1] = "|"

        board[0][0] = "+"
        board[self.height-1][self.width-1] = "+"
        board[self.height-1][0] = "+"
        board[0][self.width-1] = "+"

        return board

    def render(self):
        board = self.board_matrix()
        for x in range(len(self.snake.body)):
            x_coord, y_coord = self.snake.body[x]
            board[x_coord][y_coord] = "o"
        
        x_coord_head, y_coord_head = self.snake.head()
        board[x_coord_head][y_coord_head] = "x"
        
        for y in range(self.height):
            print("".join(board[y]))  # Join elements of each row into a single string

game = Game(10, 20)
game.render()
