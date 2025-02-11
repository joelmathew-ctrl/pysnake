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

    def take_step(self, apple, board):
        x_coord_head, y_coord_head = self.head()

        # Calculate new head position based on direction
        if self.direction == UP:
            new_head = (x_coord_head - 1, y_coord_head)
        elif self.direction == DOWN:
            new_head = (x_coord_head + 1, y_coord_head)
        elif self.direction == LEFT:
            new_head = (x_coord_head, y_coord_head - 1)
        elif self.direction == RIGHT:
            new_head = (x_coord_head, y_coord_head + 1)

        # Wrap around the board if necessary
        new_head = (
            new_head[0] % game.height,
            new_head[1] % game.width
        )

        # Check for self-collision
        if new_head in self.body:
            return True  # Collision detected, game lost

        # Check if the new head position is the apple's position
        if new_head == (apple.x_coord, apple.y_coord):
            self.increase_body_length()
            
            # Ensure apple spawns in a valid position
            while True:
                apple.x_coord = random.randint(0, game.height - 1)
                apple.y_coord = random.randint(0, game.width - 1)
                if (apple.x_coord, apple.y_coord) not in self.body:
                    break  # Ensures apple does not spawn on the snake
        else:
            # Normal movement (shift forward)
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

    def tail(self):
        return self.body[0]

    def increase_body_length(self):
        tail_x, tail_y = self.tail()
        prev_x, prev_y = self.body[1]  # Second segment (to determine tail direction)

        # Determine growth direction by extending the tail backward
        new_segment = (tail_x + (tail_x - prev_x), tail_y + (tail_y - prev_y))

        self.body.insert(0, new_segment)


class Apple:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def position_is_empty(self, board):
        if (board[self.x_coord-1][self.y_coord-1] == " "):
            return True
        else:
            return False


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(1,1), (2,1), (3,1), (4,1)], DOWN)
        self.apple = Apple(random.randint(0, height - 1), random.randint(0, width - 1))

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
        return (input("Enter the direction the snake should move in and press enter (W/A/S/D): "))

    def render(self):
        board = self.board_matrix()
        for x in range(len(self.snake.body)):
            x_coord, y_coord = self.snake.body[x]
            board[x_coord][y_coord] = "o"
        
        x_coord_head, y_coord_head = self.snake.head()
        board[x_coord_head][y_coord_head] = "x"
        
        while self.apple.position_is_empty(board) == False:
            self.apple.x_coord = random.randint(1, self.height-1)
            self.apple.y_coord = random.randint(1, self.width-1)

        board[self.apple.x_coord][self.apple.y_coord] = "*"
        
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
            gameLost = game.snake.take_step(game.apple, game.board_matrix())
    elif direction == "S" or direction == "s":
        if game.snake.set_direction(DOWN):
            gameLost = game.snake.take_step(game.apple, game.board_matrix())
    elif direction == "A" or direction == "a":
        if game.snake.set_direction(LEFT):
            gameLost = game.snake.take_step(game.apple, game.board_matrix())
    elif direction == "D" or direction == "d":
        if game.snake.set_direction(RIGHT):
            gameLost = game.snake.take_step(game.apple, game.board_matrix())
    else:
        print("Invalid input.")
    
    if gameLost:
        print("\nOops! You just became your own worst enemy. 🐍💀 Game Over!")
        time.sleep(3)
    
    time.sleep(0.5)
    clear_terminal()

