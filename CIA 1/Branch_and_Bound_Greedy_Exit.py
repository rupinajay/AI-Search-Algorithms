import heapq

def branch_and_bound_greedy_exit(graph, start, goal, cost_func, heuristic, exit_threshold):
    queue = [(0 + heuristic(start, goal), 0, [start])]
    best_cost = float('inf')
    best_path = None
    iterations = 0
    
    while queue:
        iterations += 1
        if iterations > exit_threshold:
            return best_path  # Exit if threshold is reached
        
        (_, cost, path) = heapq.heappop(queue)
        node = path[-1]
        
        if node == goal:
            if cost < best_cost:
                best_cost = cost
                best_path = path
            return best_path  # Exit immediately when a solution is found
        
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                new_path = path + [neighbor]
                new_cost = cost + cost_func(node, neighbor)
                if new_cost < best_cost:
                    priority = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(queue, (priority, new_cost, new_path))
    
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

def heuristic(node, goal):
    return ord(goal) - ord(node)

start = 'A'
goal = 'G'
exit_threshold = 10

result = branch_and_bound_greedy_exit(graph, start, goal, cost_func, heuristic, exit_threshold)
print("Branch and Bound Greedy with Exit path:", result)