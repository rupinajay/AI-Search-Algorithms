# AI Search Algorithms - CIA 1 & 2

## Overview

The **AI Search Algorithms** project is a comprehensive collection of search algorithms implemented in Python. This repository serves as an educational resource for understanding various search techniques used in artificial intelligence, including both uninformed and informed search strategies. The goal is to provide clear implementations and explanations of each algorithm, making it easier for learners and practitioners to grasp the underlying concepts.

## Table of Contents

- [Features](#features)
- [Algorithms Included](#algorithms-included)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Diverse Algorithms**: Implements a variety of search algorithms, including both uninformed and informed strategies.
- **Educational Resource**: Each algorithm is documented with explanations and examples to facilitate learning.
- **Modular Design**: Each algorithm is contained within its own Python file for easy navigation and testing.
- **Open Source**: Contributions are welcome from the community to enhance the repository further.

## Algorithms Included

### Uninformed Search Algorithms

1. **Breadth-First Search (BFS)**  
   - **File**: `BFS.py`  
   - **Description**: Explores all nodes at the present depth prior to moving on to nodes at the next depth level.

2. **Depth-First Search (DFS)**  
   - **File**: `DFS.py`  
   - **Description**: Explores as far as possible along each branch before backtracking.

3. **Uniform Cost Search (UCS)**  
   - **File**: `UCS.py`  
   - **Description**: Expands the least costly node first, ensuring the shortest path is found.

4. **Branch and Bound**  
   - **File**: `Branch_and_Bound.py`  
   - **Description**: Systematically enumerates candidate solutions by means of a tree structure.

### Informed Search Algorithms

1. **A* Search**  
   - **File**: `A_star.py`  
   - **Description**: Combines features of UCS and Greedy Best-First Search, using heuristics to improve efficiency.

2. **Greedy Best-First Search**  
   - **File**: `BMS.py`  
   - **Description**: Expands the node that appears to be closest to the goal based on a heuristic.

3. **Beam Search**  
   - **File**: `Beam_Search.py`  
   - **Description**: A variant of best-first search that limits the number of nodes expanded at each level.

### Additional Techniques

1. **Hill Climbing**  
   - **File**: `Hill_Climbing.py`  
   - **Description**: An optimization algorithm that continuously moves towards the highest value (or lowest cost) neighbor.

2. **Branch and Bound Variants**
   - Greedy: `Branch_and_Bound_Greedy.py`
   - Greedy with Exit: `Branch_and_Bound_Greedy_Exit.py`
   - Greedy with Heuristic: `Branch_and_Bound_Greedy_Heuristic.py`
   - Heuristic: `Branch_and_Bound_Heuristic.py`

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/rupinajay/AI-Search-Algorithms.git
   ```

2. Navigate into the project directory:
   ```bash
   cd AI-Search-Algorithms
   ```

3. Install any required dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Each algorithm is implemented in its own Python file. You can run them individually to see how they work. For example, to run the A* search algorithm, use:

```bash
python A_star.py
```

### Example Usage

Here’s a brief example of how you might call one of the algorithms:

```python
from A_star import AStar

# Initialize your problem here
problem = YourProblemClass()

# Create an instance of AStar
search = AStar(problem)

# Execute the search
solution = search.execute()

print("Solution found:", solution)
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional algorithms to include, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request detailing your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project is inspired by various resources on artificial intelligence and search algorithms, including textbooks, online courses, and open-source contributions from the community. Special thanks to all contributors for their efforts in enhancing this repository.

---

Feel free to modify this README further based on specific details or additional features you may want to highlight in your project!