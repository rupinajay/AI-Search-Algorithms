import heapq

def beam_search(graph, start, goal, beam_width, heuristic):
    beam = [(heuristic(start, goal), [start])]
    
    while beam:
        new_beam = []
        for _, path in beam:
            current = path[-1]
            if current == goal:
                return path
            for neighbor in graph.get(current, []):
                new_path = path + [neighbor]
                new_beam.append((heuristic(neighbor, goal), new_path))
        
        beam = heapq.nsmallest(beam_width, new_beam)
        
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
beam_width = 2

result = beam_search(graph, start, goal, beam_width, heuristic)
print("Beam Search path:", result)