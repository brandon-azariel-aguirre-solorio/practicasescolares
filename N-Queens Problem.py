def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []

    def is_safe(placement, row, col):
        for r in range(row):
            c = placement[r]
          
            if c == col:
                return False
    
            if abs(r - row) == abs(c - col):
                return False
        return True

    def backtrack(row, placement):
        if row == n:
            solutions.append(placement[:])
            return

        for col in range(n):
            if is_safe(placement, row, col):
                placement.append(col)
                backtrack(row + 1, placement)
                placement.pop()

    backtrack(0, [])
    return solutions
