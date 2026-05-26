from abc import ABC, abstractmethod
import abc
import random
class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        selected_move = random.choice(self.moves)
        
        new_x = self.position[0] + selected_move[0]
        new_y = self.position[1] + selected_move[1]
        
        self.position = (new_x, new_y)
        
        self.path.append(self.position)
        
        return self.position

    @abc.abstractmethod
    def level_up(self):
        """Abstract method to be implemented in concrete classes."""
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        
        self.moves = [
            (0, 1),   # Up
            (0, -1),  # Down
            (-1, 0),  # Left
            (1, 0)    # Right
        ]

    def level_up(self):
        diagonal_moves = [
            (-1, 1),  # Up-Left
            (1, 1),   # Up-Right
            (-1, -1), # Down-Left
            (1, -1)   # Down-Right
        ]
        self.moves.extend(diagonal_moves)
