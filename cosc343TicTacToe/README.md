# TicTacToe Minimax Agent

## Task Description

The main task for this project was to implement a minimax search algorithm into the `my_agent.py` file to create an intelligent TicTacToe playing agent. This agent competes against other agents or human players in a TicTacToe game environment provided by `cosc343TicTacToe.py`.

## Objective

The goal was to create an agent that uses the minimax algorithm to make optimal moves in a game of TicTacToe. The minimax algorithm is a decision-making algorithm used in two-player turn-based games, which helps in finding the optimal move by considering all possible future game states.

## Implementation Details

The minimax algorithm was implemented in the `TicTacToeAgent` class within `my_agent.py`. Key aspects of the implementation include:

1. **Depth-Limited Search**: The algorithm uses a maximum depth to limit the search space and improve efficiency.

2. **State Evaluation**: The `evaluate()` function from `cosc343TicTacToe.py` is used to assess the value of game states.

3. **Symmetry Reduction**: The `remove_symmetries()` function is utilized to eliminate redundant board states, reducing the search space.

4. **Recursive Minimax**: The core of the algorithm is implemented in the `minimax()` method, which recursively evaluates game states.

5. **Best Move Selection**: The `AgentFunction()` method uses the minimax algorithm to select the best move for the agent.

## Usage

To use this agent:

1. Ensure `my_agent.py` is in the same directory as `cosc343TicTacToe.py`.
2. In `settings.py`, set `player1File` or `player2File` to `"my_agent.py"`.
3. Run `cosc343TicTacToe.py` to start a game with the minimax agent.

## Future Improvements

Potential enhancements to the agent could include:

- Implementing alpha-beta pruning to further optimize the search.
- Adding a transposition table to cache evaluated states.
- Tweaking the evaluation function for better performance.

## Acknowledgements

This project was part of the COSC343/AIML402 course at the University of Otago. The game environment and helper functions were provided by the course instructors.