# PySnake - A Simple Snake Game in Python

## Overview
PySnake is a classic snake game implemented in Python. The game involves controlling a snake to eat apples, which makes the snake grow longer. The game ends if the snake collides with itself. The game is played in the terminal and features a customizable game board size.

## Features
- **Customizable Game Board**: Set the height and width of the game board.
- **Simple Controls**: Use `W`, `A`, `S`, `D` keys to control the snake's direction.
- **Terminal-Based**: Play the game directly in your terminal.
- **Dynamic Apple Spawning**: Apples spawn randomly on the board, ensuring they don't overlap with the snake.

## Requirements
- Python 3.x
- `numpy` library

## Installation
1. Clone the repository or download the `snek.py` file.
2. Ensure you have Python 3.x installed on your system.
3. Install the required `numpy` library using pip:
   ```bash
   pip install numpy
   ```

## How to Play
1. Run the `snek.py` script:
   ```bash
   python snek.py
   ```
2. Enter the desired height and width for the game board when prompted. The values must be greater than 5.
3. Use the following keys to control the snake:
   - `W` or `w`: Move Up
   - `S` or `s`: Move Down
   - `A` or `a`: Move Left
   - `D` or `d`: Move Right
4. The game ends if the snake collides with itself.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.


Enjoy playing PySnake! 🐍