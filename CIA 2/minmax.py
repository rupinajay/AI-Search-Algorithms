
def minimax(depth, nodeIndex, isMaximizingPlayer, values):

    if depth == 3:
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = float('-inf')

        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values)
            best = max(best, val)
        return best
    else:
        best = float('inf')

        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values)
            best = min(best, val)
        return best


if __name__ == "__main__":

    values = [1, 4, 7, 2, 3, 0, 6, 5]

    optimalValue = minimax(0, 0, True, values)

    print(f"Optimal value using Minimax: {optimalValue}")
