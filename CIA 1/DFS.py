def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph.get(vertex, []):
                stack.append((neighbor, path + [neighbor]))
    return None

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

start = 'A'
goal = 'G'

result = dfs(graph, start, goal)
print("DFS path:", result)