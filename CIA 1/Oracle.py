def oracle(graph, start, goal):
    # In a real scenario, this would be replaced with domain-specific knowledge
    optimal_path = ['A', 'B', 'E', 'G']  # Hardcoded for this example
    return optimal_path if optimal_path[0] == start and optimal_path[-1] == goal else None

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

result = oracle(graph, start, goal)
print("Oracle path:", result)