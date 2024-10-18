import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random

# Create a sample graph
G = nx.Graph()

# Add nodes and edges with weights
edges = [
    ('A', 'B', 1), ('A', 'C', 4), ('B', 'D', 2), 
    ('C', 'D', 3), ('C', 'E', 5), ('D', 'E', 1), 
    ('E', 'F', 2), ('F', 'G', 3)
]
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Visualize the graph
def visualize_graph(G, path=None):
    pos = nx.spring_layout(G)  # Position layout for nodes
    plt.figure(figsize=(10, 6))
    
    # Draw nodes and labels
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold')
    
    # Draw edge weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # If there's a path, highlight it in red
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
    
    st.pyplot(plt)

# Implementing Search Algorithms
# 1. BFS (Breadth-First Search)
def bfs(G, start, goal):
    visited = set()
    queue = [[start]]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node == goal:
            return path
        
        elif node not in visited:
            for neighbor in G[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
            visited.add(node)

# 2. DFS (Depth-First Search)
def dfs(G, start, goal):
    visited = set()
    stack = [[start]]
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node == goal:
            return path
        
        elif node not in visited:
            for neighbor in G[node]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
                
            visited.add(node)

# 3. Hill Climbing
def hill_climbing(G, start, goal):
    current = start
    path = [start]

    while current != goal:
        # Get neighbors of the current node
        neighbors = list(G.neighbors(current))
        
        # If there are no neighbors, break (dead end)
        if not neighbors:
            break
        
        # Choose the neighbor that has the lowest edge weight to current
        next_node = min(neighbors, key=lambda x: G[current][x]['weight'])
        
        # If the next node is already in the path (loop), break
        if next_node in path:
            break
        
        # Add to the path and move to the next node
        path.append(next_node)
        current = next_node

    # If we reach the goal, return the path
    if current == goal:
        return path
    else:
        return None  # Return None if the goal is not reached
    
# 4. Beam Search (k = 2)
def beam_search(G, start, goal, k=2):
    queue = [(start, [start])]
    
    while queue:
        next_queue = []
        for node, path in queue:
            if node == goal:
                return path
            
            neighbors = list(G.neighbors(node))
            neighbors.sort(key=lambda x: G[node][x]['weight'])
            
            for neighbor in neighbors[:k]:
                next_queue.append((neighbor, path + [neighbor]))
                
        queue = next_queue
    
    return None

# 5. A* Algorithm
def a_star(G, start, goal, heuristic):
    queue = [(0, start, [])]
    visited = set()
    
    while queue:
        cost, node, path = heapq.heappop(queue)
        
        if node == goal:
            return path + [goal]
        
        if node not in visited:
            visited.add(node)
            path = path + [node]
            
            for neighbor in G.neighbors(node):
                total_cost = cost + G[node][neighbor]['weight'] + heuristic[neighbor]
                heapq.heappush(queue, (total_cost, neighbor, path))
                
    return None

# 6. Branch and Bound
def branch_and_bound(G, start, goal):
    queue = [(start, [start])]
    best_path = None
    min_cost = float('inf')
    
    while queue:
        node, path = queue.pop(0)
        
        if node == goal:
            path_cost = sum(G[u][v]['weight'] for u, v in zip(path, path[1:]))
            if path_cost < min_cost:
                best_path = path
                min_cost = path_cost
                
        for neighbor in G.neighbors(node):
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    
    return best_path

# 7. Greedy Branch and Bound
def greedy_branch_and_bound(G, start, goal):
    queue = [(start, [start])]
    best_path = None
    min_cost = float('inf')
    
    while queue:
        node, path = queue.pop(0)
        
        if node == goal:
            path_cost = sum(G[u][v]['weight'] for u, v in zip(path, path[1:]))
            if path_cost < min_cost:
                best_path = path
                min_cost = path_cost
                
        for neighbor in G.neighbors(node):
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    
    return best_path

# 8. Greedy with Exit (assumes exit node is G)
def greedy_with_exit(G, start):
    current = start
    path = [start]
    
    while True:
        neighbors = list(G.neighbors(current))
        if not neighbors:
            break
        next_node = min(neighbors, key=lambda x: G[current][x]['weight'])
        path.append(next_node)
        current = next_node
        if current == 'G':  # Exit condition
            break
        
    return path

# 9. Greedy with Heuristic
def greedy_with_heuristic(G, start, goal, heuristic):
    queue = [(0, start, [])]
    visited = set()
    
    while queue:
        _, node, path = heapq.heappop(queue)
        
        if node == goal:
            return path + [goal]
        
        if node not in visited:
            visited.add(node)
            path = path + [node]
            
            for neighbor in G.neighbors(node):
                total_cost = G[node][neighbor]['weight'] + heuristic[neighbor]
                heapq.heappush(queue, (total_cost, neighbor, path))
                
    return None

# 10. Heuristic Branch and Bound
def heuristic_branch_and_bound(G, start, goal, heuristic):
    queue = [(0, start, [])]
    best_path = None
    min_cost = float('inf')
    
    while queue:
        cost, node, path = heapq.heappop(queue)
        
        if node == goal:
            path_cost = sum(G[u][v]['weight'] for u, v in zip(path, path[1:]))
            if path_cost < min_cost:
                best_path = path
                min_cost = path_cost
                
        for neighbor in G.neighbors(node):
            if neighbor not in path:
                total_cost = cost + G[node][neighbor]['weight'] + heuristic[neighbor]
                heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))
    
    return best_path

# 11. Oracle (Simulates best path based on optimal data)
def oracle_search(G, start, goal):
    return nx.shortest_path(G, start, goal, weight='weight')

# 12. A* with Heuristic
def a_star_with_heuristic(G, start, goal, heuristic):
    queue = [(0, start, [])]
    visited = set()
    
    while queue:
        cost, node, path = heapq.heappop(queue)
        
        if node == goal:
            return path + [goal]
        
        if node not in visited:
            visited.add(node)
            path = path + [node]
            
            for neighbor in G.neighbors(node):
                total_cost = cost + G[node][neighbor]['weight'] + heuristic[neighbor]
                heapq.heappush(queue, (total_cost, neighbor, path))
                
    return None

# Define Heuristic for A* and other algorithms
heuristic = {node: random.randint(1, 10) for node in G.nodes()}

# Define the Streamlit app
st.title("Graph Search Algorithms Visualization")

start = st.selectbox("Select Start Node", G.nodes())
goal = st.selectbox("Select Goal Node", G.nodes())

algorithm = st.selectbox("Select Algorithm", [
    "BFS", "DFS", "Hill Climbing", "Beam Search", 
    "A*", "Branch and Bound", "Greedy Branch and Bound",
    "Greedy with Exit", "Greedy with Heuristic", 
    "Heuristic Branch and Bound", "Oracle", "A* with Heuristic"
])

if st.button("Find Path"):
    if algorithm == "BFS":
        path = bfs(G, start, goal)
    elif algorithm == "DFS":
        path = dfs(G, start, goal)
    elif algorithm == "Hill Climbing":
        path = hill_climbing(G, start, goal)  # No heuristic here
    elif algorithm == "Beam Search":
        path = beam_search(G, start, goal)
    elif algorithm == "A*":
        path = a_star(G, start, goal, heuristic)
    elif algorithm == "Branch and Bound":
        path = branch_and_bound(G, start, goal)
    elif algorithm == "Greedy Branch and Bound":
        path = greedy_branch_and_bound(G, start, goal)
    elif algorithm == "Greedy with Exit":
        path = greedy_with_exit(G, start)
    elif algorithm == "Greedy with Heuristic":
        path = greedy_with_heuristic(G, start, goal, heuristic)
    elif algorithm == "Heuristic Branch and Bound":
        path = heuristic_branch_and_bound(G, start, goal, heuristic)
    elif algorithm == "Oracle":
        path = oracle_search(G, start, goal)
    elif algorithm == "A* with Heuristic":
        path = a_star_with_heuristic(G, start, goal, heuristic)
    
    if path:
        st.write(f"Path found: {path}")
        visualize_graph(G, path)
    else:
        st.write("No path found")
else:
    visualize_graph(G)
