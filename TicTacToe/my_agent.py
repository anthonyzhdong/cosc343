__author__ = "Lech Szymanski"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "lech.szymanski@otago.ac.nz"

# Import the random number generation library
import random
from cosc343TicTacToe import maxs_possible_moves ,\
mins_possible_moves ,\
terminal , evaluate ,\
state_change_to_action ,\
remove_symmetries

class TicTacToeAgent():
    """
           A class that encapsulates the code dictating the
           behaviour of the TicTacToe playing agent

           Methods
           -------
           AgentFunction(percepts)
               Returns the move made by the agent given state of the game in percepts
           """

    def __init__(self, h):
        """Initialises the agent

        :param h: Handle to the figures showing state of the board -- only used
                  for human_agent.py to enable selecting next move by clicking
                  on the matplotlib figure.
        """
        pass

    

    def AgentFunction(self, percepts):
        """The agent function of the TicTacToe agent -- returns action
         relating the row and column of where to make the next move

        :param percepts: the state of the board a list of rows, each
        containing a value of three columns, where 0 identifies the empty
        suare, 1 is a square with this agent's mark and -1 is a square with
        opponent's mark
        :return: tuple (r,c) where r is the row and c is the column index
                 where this agent wants to place its mark
        """
        max_depth = 9 # max depth of the tree (9 for full tictactoe game)
        # initial values for best score and move
        best_score = float('-inf')
        best_move = None
        # generate all possible moves for agent then remove symmetries
        max_moves = remove_symmetries(maxs_possible_moves(percepts))

        # iterate through each move, call minimax and find best move
        for potential_move in max_moves:
            # call minimax for each move
            score = self.minimax(potential_move, 0, False, max_depth)
            if score > best_score:
                best_score = score
                best_move = potential_move

        r, c = state_change_to_action(percepts, best_move)
        return r,c
    
    # maximum score = best possible move (score) for our agent
    # minimum score = worse possible move (score) for our agent as it's the opponents turn
    def minimax(self, state, depth, is_agent_turn, max_depth):
        # base case if terminal state or max depth reached
        if terminal(state) or depth == max_depth:
            return evaluate(state)
        
        # checks if it's our turn
        if is_agent_turn:
            best_max_score = float('-inf')
            unique_moves = remove_symmetries(maxs_possible_moves(state))
            # recursively evaluate the move, switching to opponent's turn
            for move in unique_moves:
                move_score = self.minimax(move, depth + 1, False, max_depth)
                best_max_score = max(best_max_score, move_score)
            return best_max_score
        else:
            best_min_score = float('inf')
            unique_moves = remove_symmetries(mins_possible_moves(state))
            for move in unique_moves:
                move_score = self.minimax(move, depth + 1, True, max_depth)
                best_min_score = min(best_min_score, move_score)
            return best_min_score
        

