def hill_climbing(graph, h, start, goal):
    current = start
    path = [current]

    print("=== STARTING HILL CLIMBING SEARCH (MANHATTAN) ===")
    
    while current != goal:
        neighbors = graph[current]

        if not neighbors:
            print("No neighbors found. Search failed.")
            return path

        best_neighbor = min(neighbors, key=lambda node: h[node])

        print(
            f"Current Node: {current} (h={h[current]}) "
            f"--> Best Neighbor: {best_neighbor} (h={h[best_neighbor]})"
        )

        if h[best_neighbor] >= h[current]:
            print("Local optimum reached. Halting search.")
            break

        current = best_neighbor
        path.append(current)

    if current == goal:
        print("Success! Goal reached.")
    else:
        print("Failed to reach the goal.")

    return path


if __name__ == "__main__":
    graph = {
        'S': ['C', 'H', 'I', 'K'],
        'A': ['B', 'C', 'D'],
        'B': ['A', 'F'],
        'C': ['A', 'D', 'H', 'S'],
        'D': ['A', 'C', 'F', 'H'],
        'E': ['I', 'L'],
        'F': ['B', 'D', 'H', 'J'],
        'H': ['C', 'D', 'F', 'K', 'S'],
        'I': ['E', 'N', 'O', 'L', 'S'],
        'J': ['F', 'G', 'M'],
        'K': ['H', 'N', 'S'],
        'L': ['E', 'I', 'O'],
        'M': ['J', 'G', 'P'],
        'N': ['I', 'K', 'O', 'R'],
        'O': ['I', 'N', 'L'],
        'P': ['M', 'G', 'Q'],
        'Q': ['R', 'P', 'G'],
        'R': ['Q', 'N'],
        'G': ['J', 'M', 'P', 'Q']
    }

    h_manhattan = {
        'S': 12,
        'A': 9,
        'B': 10,
        'C': 13,
        'D': 9,
        'E': 17,
        'F': 6,
        'H': 9,
        'I': 11,
        'J': 2,
        'K': 5,
        'L': 14,
        'M': 4,
        'N': 6,
        'O': 11,
        'P': 4,
        'Q': 4,
        'R': 6,
        'G': 0
    }

    # Run Hill Climbing Search
    final_path = hill_climbing(graph, h_manhattan, start='S', goal='G')
    print("Final Traversed Path:", final_path)