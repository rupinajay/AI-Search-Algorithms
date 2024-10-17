import heapq

def branch_and_bound(graph, start, goal, cost_func):
    queue = [(0, [start])]
    best_cost = float('inf')
    best_path = None
    
    while queue:
        (cost, path) = heapq.heappop(queue)
        node = path[-1]
        
        if node == goal:
            if cost < best_cost:
                best_cost = cost
                best_path = path
            continue
        
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                new_path = path + [neighbor]
                new_cost = cost + cost_func(node, neighbor)
                if new_cost < best_cost:
                    heapq.heappush(queue, (new_cost, new_path))
    
    return best_path

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

def cost_func(node1, node2):
    return 1  # Assuming uniform cost for simplicity

start = 'A'
goal = 'G'

result = branch_and_bound(graph, start, goal, cost_func)
print("Branch and Bound path:", result)