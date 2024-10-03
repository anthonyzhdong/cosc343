from cosc343EightPuzzle import EightPuzzle
import time

class Node:
    def __init__(self, s, parent=None, g=0, h=0, action=None):
        self.s = tuple(s)  # Convert state to tuple for hashability
        self.parent = parent
        self.g = g
        self.f = g + h
        self.action = action

def manhattan_distance(s, goal):
    distance = 0
    for i in range(len(s)):
        if s[i] != 0:  # Skip the empty tile
            current_row, current_col = divmod(i, 3)
            goal_position = goal.index(s[i])
            goal_row, goal_col = divmod(goal_position, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def astar_graph_search(puzzle, init_state, goal_state):
    root_node = Node(s=init_state, h=manhattan_distance(init_state, goal_state))
    fringe = [root_node]
    visited = set()

    while fringe:
        current_node = min(fringe, key=lambda x: x.f)
        fringe.remove(current_node)

        if current_node.s == tuple(goal_state):
            return current_node

        if current_node.s in visited:
            continue

        visited.add(current_node.s)

        available_actions = puzzle.actions(s=current_node.s)
        for a in available_actions:
            next_state = puzzle.step(s=current_node.s, a=a)
            if tuple(next_state) not in visited:
                new_node = Node(s=next_state,
                                parent=current_node,
                                g=current_node.g + 1,
                                h=manhattan_distance(next_state, goal_state),
                                action=a)
                fringe.append(new_node)

    return None

def get_solution_path(node):
    path = []
    while node.parent:
        path.append(node.action)
        node = node.parent
    return list(reversed(path))

# Main execution
puzzle = EightPuzzle(mode='hard')
init_state = puzzle.reset()
goal_state = puzzle.goal()

start_time = time.time()

solution_node = astar_graph_search(puzzle, init_state, goal_state)

elapsed_time = time.time() - start_time

if solution_node is None:
    print("Didn't find a solution!!!")
else:
    action_sequence = get_solution_path(solution_node)
    print(f"Number of moves: {len(action_sequence)}")
    print(f"Elapsed time: {elapsed_time:.1f} seconds")
    puzzle.show(s=init_state, a=action_sequence)