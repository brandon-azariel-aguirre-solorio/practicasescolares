adjacency_matrix = [
    [0, 1, 1, 1],  # The neighbors of A are B, C, and D
    [1, 0, 0, 1],  # The neighbors of B are A and D
    [1, 0, 0, 0],  # The only neighbor of C is A
    [1, 1, 0, 0]   # The neighbors of D are A and B
]

adjacency_list = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['A', 'B']
}
adjacency_list = [
    ['B', 'C', 'D'],  # Neighbors of A (index 0)
    ['A', 'D'],       # Neighbors of B (index 1)
    ['A'],            # Neighbors of C (index 2)
    ['A', 'B']        # Neighbors of D (index 3)
]
