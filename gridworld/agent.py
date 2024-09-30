from cosc343GridWorld import GridWorldEnvironment
import numpy as np
import matplotlib.pyplot as plt

# Initialize the environment
env = GridWorldEnvironment()

# Set hyperparameters
T = 0.1  # Temperature for exploration (lower values: less exploration)
gamma = 0.7  # Discount factor
alpha = 0.3  # Learning rate
num_episodes = 1000
max_steps_per_episode = 100

# Initialize Q-table as a dictionary
Q = dict()

# Function to print Q-table
def print_q_table(Q):
    print("\nFinal Q-table:")
    print("State\t\tN\t\tE\t\tS\t\tW")
    for state in sorted(Q.keys()):
        print(f"{state}\t{Q[state][0]:.4f}\t{Q[state][1]:.4f}\t{Q[state][2]:.4f}\t{Q[state][3]:.4f}")


# Main training loop
for episode in range(num_episodes):
    s, R = env.reset()
    
    for step in range(max_steps_per_episode):
        # Ensure state is in Q-table
        if s not in Q:
            Q[s] = np.zeros(env.num_actions)
        
        # Choose action using epsilon-greedy policy
        if np.random.rand() < 0.1:  # 10% chance of random action
            a = np.random.randint(env.num_actions)
        else:
            qvalues = Q[s]
            p = qvalues - np.min(qvalues)
            p = np.exp(p/T)
            p = p/np.sum(p)
            a = np.random.choice(env.num_actions, p=p)
        
        # Take action and observe next state and reward
        s_prime, R_prime = env.step(a)
        
        # Update Q-table
        if env.terminal():
            Q[s][a] = R_prime
        else:
            if s_prime not in Q:
                Q[s_prime] = np.zeros(env.num_actions)
            Q[s][a] += alpha * (R_prime + gamma * np.max(Q[s_prime]) - Q[s][a])
        
        # Render environment (uncomment to visualize)
       # env.render(Q=Q, a=a, titleStr=f'Episode {episode+1}, Step {step+1}')
        
        # Move to next state
        s = s_prime
        
        if env.terminal():
            break

# Print the final Q-table
print_q_table(Q)

# Display final policy
env.render(Q=Q, policy=True)

# Keep the plot window open
plt.show()