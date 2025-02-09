# Name: snek.py
# Author: Joel Mathew

import numpy as np 
import os
import time

# Defining directions 
UP = (0,1)
DOWN = (0,-1)
LEFT = (-1,0)
RIGHT = (1,0)

# Function to clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self):
        x_coord_head, y_coord_head = self.head()
        if (self.direction == UP):
            self.body = self.body[1:] + [(x_coord_head - 1, y_coord_head)]
        elif (self.direction == DOWN):
            self.body = self.body[1:] + [(x_coord_head + 1, y_coord_head)]
        elif (self.direction == LEFT):
            self.body = self.body[1:] + [(x_coord_head, y_coord_head - 1)]
        elif (self.direction == RIGHT):
            self.body = self.body[1:] + [(x_coord_head, y_coord_head + 1)]


    def set_direction(self, direction):
        if (self.direction == UP and direction == DOWN) or \
        (self.direction == DOWN and direction == UP) or \
        (self.direction == RIGHT and direction == LEFT) or \
        (self.direction == LEFT and direction == RIGHT):
            return False # Ignore invalid direction change
        self.direction = direction
        return True


    def head(self):
        return self.body[-1]

class Apple:
    pass

class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(1,1), (2,1), (3,1), (4,1)], DOWN)

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

    def get_user_input(self):
        return (input("Enter the direction the snake should move in and press enter: (W/A/S/D)"))

    def render(self):
        board = self.board_matrix()
        for x in range(len(self.snake.body)):
            x_coord, y_coord = self.snake.body[x]
            board[x_coord][y_coord] = "o"
        
        x_coord_head, y_coord_head = self.snake.head()
        board[x_coord_head][y_coord_head] = "x"
        
        # Print the board 
        for y in range(self.height):
            print("".join(board[y]))  # Join elements of each row into a single string

game = Game(10, 20)
gameLost = False
while gameLost == False:
    game.render()
    direction = game.get_user_input()
    
    if (direction == "W" or direction == "w"):
        if (game.snake.set_direction(UP) == True):
            game.snake.take_step()
    elif (direction == "S" or direction == "s"):
        if (game.snake.set_direction(DOWN) == True):
            game.snake.take_step()
    elif (direction == "A" or direction == "a"):
        if (game.snake.set_direction(LEFT) == True):
            game.snake.take_step()
    elif (direction == "D" or direction == "d"):
        if (game.snake.set_direction(RIGHT) == True):
            game.snake.take_step()

    else:
        print("Invalid input.")
    time.sleep(0.5)
    clear_terminal()
