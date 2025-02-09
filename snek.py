# Name: snek.py
# Author: Joel Mathew

import numpy as np 
import os
import time
import random

# Defining directions 
UP = (0,1)
DOWN = (0,-1)
LEFT = (-1,0)
RIGHT = (1,0)

# Function to clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))  # Try to convert input to integer
            if value <= 5:  # Ensure the value is greater than 5
                print("Please enter a number greater than 5.")
            else:
                return value
        except ValueError:  # Handle non-integer inputs
            print("Invalid input. Please enter a valid integer.")

class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self):
        x_coord_head, y_coord_head = self.head()

        if self.direction == UP:
            x_coord_head = (x_coord_head - 1) % game.height
        elif self.direction == DOWN:
            x_coord_head = (x_coord_head + 1) % game.height
        elif self.direction == LEFT:
            y_coord_head = (y_coord_head - 1) % game.width
        elif self.direction == RIGHT:
            y_coord_head = (y_coord_head + 1) % game.width

        new_head = (x_coord_head, y_coord_head)

        # Check for self-collision
        if new_head in self.body:
            return True  # Collision detected, game lost

        self.body = self.body[1:] + [new_head]
        return False  # No collision, game continues




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

# Get valid height and width for the map
game_height = get_valid_input("Enter the height of the map: ")
game_width = get_valid_input("Enter the width of the map: ")

print(f"Game map dimensions: Height = {game_height}, Width = {game_width}")

game = Game(game_height, game_width)
gameLost = False
while not gameLost:
    game.render()
    direction = game.get_user_input()
    
    if direction == "W" or direction == "w":
        if game.snake.set_direction(UP):
            gameLost = game.snake.take_step()
    elif direction == "S" or direction == "s":
        if game.snake.set_direction(DOWN):
            gameLost = game.snake.take_step()
    elif direction == "A" or direction == "a":
        if game.snake.set_direction(LEFT):
            gameLost = game.snake.take_step()
    elif direction == "D" or direction == "d":
        if game.snake.set_direction(RIGHT):
            gameLost = game.snake.take_step()
    else:
        print("Invalid input.")
    
    if gameLost:
        print("\nOops! You just became your own worst enemy. 🐍💀 Game Over!")
        time.sleep(3)
    
    time.sleep(0.5)
    clear_terminal()

