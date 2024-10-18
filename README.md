# AI Search Algorithms

## Overview

The **AI Search Algorithms** project implements various search algorithms on a given graph, starting from node **S** and ending at node **G**. Each algorithm finds the best path from **S** to **G** based on different strategies. The graph and heuristic values are hard-coded, but they can be modified as needed for experimentation or further customization.

## Graph Structure

The graph used in all algorithms is as follows:

```python
graph = {
    'S': {'A': 1, 'B': 2, 'C': 5},
    'A': {'D': 3, 'S': 1, 'B': 1},
    'B': {'A': 1, 'S': 2},
    'C': {'E': 4, 'S': 5},
    'D': {'A': 3, 'G': 2},
    'E': {'C': 4},
    'G': {'D': 2}
}
```
The heuristic values for each node:


```python
heuristic = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 5,
    'D': 1,
    'E': 3,
    'G': 0
}
```
## Algorithms and Expected Outputs
This project implements the following algorithms, with each producing a unique path based on the given graph structure:

1. British Museum Search
Description: A brute-force approach where all possible paths are explored.
Expected Output:
British Museum Search path: ['A', 'B', 'E', 'G']

2. Depth-First Search (DFS)
Description: DFS explores each branch of the graph as deeply as possible before backtracking.
Expected Output:
DFS path: ['A', 'C', 'F', 'G']

3. Breadth-First Search (BFS)
Description: BFS explores all nodes at the present depth level before moving on to nodes at the next depth level.
Expected Output:
BFS path: ['A', 'B', 'E', 'G']

4. Hill Climbing
Description: A greedy algorithm that always expands the node with the lowest heuristic value.
Expected Output:
Hill Climbing path: ['A', 'C', 'G']

5. Beam Search
Description: Keeps track of a limited number of best nodes at each level to reduce memory usage.
Expected Output:
Beam Search path: ['A', 'B', 'E', 'G']

6. Oracle Search
Description: Hypothetical search with perfect knowledge about the shortest path.
Expected Output:
Oracle path: ['A', 'B', 'E', 'G']

7. Branch and Bound (B&B)
Description: Explores all possible paths but prunes paths with a higher cost than the best path found so far.
Expected Output:
Branch and Bound path: ['A', 'B', 'E', 'G']

8. Branch and Bound Greedy
Description: A greedy version of Branch and Bound that uses a heuristic to guide the search.
Expected Output:
Branch and Bound Greedy path: ['A', 'C', 'F', 'G']

9. Branch and Bound Greedy with Exit
Description: A variation of B&B Greedy that exits immediately when the goal node is found.
Expected Output:
Branch and Bound Greedy with Exit path: ['A', 'C']

10. Branch and Bound Greedy with Heuristic
Description: Combines both cost and heuristic to prune the search space more aggressively.
Expected Output:
Branch and Bound Greedy with Heuristic path: ['A', 'C', 'F', 'G']

11. A* Algorithm
Description: An informed search algorithm that uses both path cost and heuristics to find the optimal path.
Expected Output:
A* algorithm path: ['A', 'C', 'F', 'G']

## Minimax Algorithm and Alpha-Beta Pruning
Minimax Algorithm
The Minimax Algorithm is used in decision-making and game theory. It alternates between two players, a Maximizer and a Minimizer. The goal is for the Maximizer to maximize their score, while the Minimizer tries to minimize it.

## Alpha-Beta Pruning
Alpha-Beta Pruning optimizes the Minimax algorithm by reducing the number of nodes evaluated, improving efficiency without losing accuracy.

Example Tree Structure:
```
          N1
        /    \
      N2      N3
     /  \    /  \
   N4   N5  N6   N7
  / \   / \ / \   / \
 1   4 7   2 3   0   6   5
```
Expected Outputs:

Minimax Algorithm: Optimal value using Minimax: 5
Alpha-Beta Pruning: Optimal value using Alpha-Beta Pruning: 5

## Conclusion
This project demonstrates the implementation and comparison of various AI search algorithms. Each algorithm provides unique insights and optimizations for solving search problems, from brute-force approaches to heuristically guided and optimal search strategies.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
This project is inspired by various resources on artificial intelligence and search algorithms, including textbooks, online courses, and open-source contributions from the community.