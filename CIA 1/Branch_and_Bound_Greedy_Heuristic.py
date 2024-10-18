import heapq

def branch_and_bound_greedy_heuristic(graph, start, goal, cost_func, heuristic):
    queue = [(0 + heuristic(start, goal), 0, [start])]
    visited = set()
    
    while queue:
        (_, cost, path) = heapq.heappop(queue)
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + cost_func(node, neighbor)
                    priority = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(queue, (priority, new_cost, new_path))
    
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

def cost_func(node1, node2):
    return 1  # Assuming uniform cost for simplicity

def heuristic(node, goal):
    return ord(goal) - ord(node)

start = 'A'
goal = 'G'

result = branch_and_bound_greedy_heuristic(graph, start, goal, cost_func, heuristic)
print("Branch and Bound Greedy with Heuristic path:", result)
