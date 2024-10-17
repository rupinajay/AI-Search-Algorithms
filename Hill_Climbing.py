def hill_climbing(graph, start, goal, heuristic):
    current = start
    path = [current]
    
    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:
            return None  # No solution found
        
        # Find the neighbor with the best heuristic value
        next_node = min(neighbors, key=lambda x: heuristic(x, goal))
        
        if heuristic(next_node, goal) >= heuristic(current, goal):
            return None  # Stuck at local maximum
        
        current = next_node
        path.append(current)
    
    return path

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

def heuristic(node, goal):
    # This is a dummy heuristic. In a real scenario, you'd use a problem-specific heuristic.
    return ord(goal) - ord(node)

start = 'A'
goal = 'G'

result = hill_climbing(graph, start, goal, heuristic)
print("Hill Climbing path:", result)