def climb_stairs_recursive(n):
    """Recursive approach"""
    if n <= 2:
        return n  # Base cases: 1 way for 1 step, 2 ways for 2 steps
    # To reach step n, we can come from step (n-1) or step (n-2)
    return climb_stairs_recursive(n-1) + climb_stairs_recursive(n-2)


def climb_stairs_memo(n, memo={}):
    """Dynamic programming with memoization"""
    # Check if we've already calculated this value
    if n in memo:
        return memo[n]  # Return cached result - O(1) lookup!
    
    # Base cases
    if n <= 2:
        return n
    
    # Calculate once and store in memo for future use
    memo[n] = climb_stairs_memo(n-1, memo) + climb_stairs_memo(n-2, memo)
    return memo[n]
