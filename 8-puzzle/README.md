# 8-Puzzle Solver

This project implements an A* search algorithm to solve the 8-puzzle problem. It was developed as part of the COSC343/AIML402 course at the University of Otago.

## Project Structure

- `cosc343EightPuzzle.py`: Contains the `EightPuzzle` class, which provides the environment for the 8-puzzle problem.
- `exercise1.py`: Implements the A* graph search algorithm to solve the 8-puzzle.

## Features

- Solves 8-puzzle problems of varying difficulty (easy, medium, hard)
- Uses A* graph search with Manhattan distance heuristic
- Visualizes the solution path

## Requirements

- Python 3.11
- NumPy
- Matplotlib

## Usage

1. Ensure you have the required libraries installed:
   ```
   pip install numpy matplotlib
   ```

2. Run the script:
   ```
   python exercise1.py
   ```

3. The script will solve the 8-puzzle problem and display:
   - Number of moves in the solution
   - Time taken to find the solution
   - Visualization of the solution path

## Customization

You can change the difficulty of the puzzle by modifying the `mode` parameter when initializing the `EightPuzzle` object in `exercise1.py`:

```python
puzzle = EightPuzzle(mode='easy')  # or 'medium' or 'hard'
```

## Implementation Details

- The A* search algorithm is implemented using a graph search approach to avoid revisiting states.
- The Manhattan distance heuristic is used to estimate the cost from the current state to the goal state.
- States are represented as tuples for efficient hashing and comparison.

## Performance

The current implementation solves the 'hard' puzzle in approximately 2 seconds on average hardware.

## Author

This project was developed as part of the COSC343/AIML402 course at the University of Otago, under the guidance of Lech Szymanski.