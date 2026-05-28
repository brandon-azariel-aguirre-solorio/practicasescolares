def dfs(adj_matrix, start_node):
    n = len(adj_matrix)
    visited = [False] * n
    result = []

    def explore(node):
        visited[node] = True
        result.append(node)

        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                explore(neighbor)

    explore(start_node)
    return result
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
