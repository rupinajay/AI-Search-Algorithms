import heapq

def branch_and_bound_heuristic(graph, start, goal, heuristic):
    queue = [(heuristic(start, goal), [start])]
    visited = set()
    
    while queue:
        (_, path) = heapq.heappop(queue)
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    priority = heuristic(neighbor, goal)
                    heapq.heappush(queue, (priority, new_path))
    
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

def heuristic(node, goal):
    return ord(goal) - ord(node)

start = 'A'
goal = 'G'

result = branch_and_bound_heuristic(graph, start, goal, heuristic)
print("Branch and Bound with Heuristic path:", result)