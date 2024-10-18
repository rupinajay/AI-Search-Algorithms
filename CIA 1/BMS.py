import random

def british_museum_search(graph, start, goal):
    path = [start]
    while path[-1] != goal:
        current = path[-1]
        if current in graph:
            next_node = random.choice(graph[current])
            path.append(next_node)
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

start = 'A'
goal = 'G'

result = british_museum_search(graph, start, goal)
print("British Museum Search path:", result)