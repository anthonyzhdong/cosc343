# Grid World Reinforcement Learning

This project implements a Q-learning algorithm to solve a Grid World problem. It was developed as part of the COSC343/AIML402 course at the University of Otago.

## Project Structure

- `cosc343GridWorld.py`: Contains the `GridWorldEnvironment` class, which provides the environment for the Grid World problem.
- `agent.py`: Implements the Q-learning algorithm to solve the Grid World problem.

## Features

- Implements Q-learning algorithm for reinforcement learning
- Visualizes the Grid World environment and the agent's actions
- Allows customization of learning parameters (temperature, discount factor, learning rate)
- Displays Q-table updates and final policy

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
   python agent.py
   ```

3. The script will run the Q-learning algorithm and display:
   - Visualization of the Grid World environment
   - Q-table updates
   - Final policy

## Customization

You can modify various parameters in the `agent.py` script to experiment with the learning process:

- `T`: Temperature for exploration (lower values: less exploration)
- `gamma`: Discount factor for future rewards
- `alpha`: Learning rate
- `num_episodes`: Number of episodes to run
- `max_steps_per_episode`: Maximum number of steps per episode

You can also modify the Grid World environment by changing the `R` parameter when initializing the environment:

```python
env = GridWorldEnvironment(R=-0.04)
```

This sets a default reward for non-terminal states, which can affect the learned policy.

## Implementation Details

- The Q-table is implemented as a dictionary for efficient state-action value storage.
- The agent uses an epsilon-greedy policy for action selection, balancing exploration and exploitation.
- The learning process uses temporal difference updates to refine Q-values.

## Visualization

The project includes visualization of:
- The Grid World environment
- The agent's current position and actions
- Q-table updates (highlighted in red when changed)
- Final learned policy

## Author

This project was developed as part of the COSC343/AIML402 course at the University of Otago.