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
    # Undirected graph representation (adjacency list) derived from the source image
    graph = {
        'S': ['C', 'A'],
        'A': ['S', 'C', 'B'],
        'C': ['S', 'A', 'B', 'G'],
        'B': ['A', 'C', 'G'],
        'G': ['C', 'B']
    }

    # Manhattan distance values to G (11, 5) based on coordinates:
    # S(0,4), A(3,0), C(5,3), B(9,1), G(11,5)
    # h(n) = |x - 11| + |y - 5|
    h_manhattan = {
        'S': 12,  # |0-11| + |4-5| = 11 + 1 = 12
        'A': 13,  # |3-11| + |0-5| = 8 + 5 = 13
        'C': 8,   # |5-11| + |3-5| = 6 + 2 = 8
        'B': 6,   # |9-11| + |1-5| = 2 + 4 = 6
        'G': 0    # |11-11| + |5-5| = 0
    }

    # Run Hill Climbing Search
    final_path = hill_climbing(graph, h_manhattan, start='S', goal='G')
    print("Final Traversed Path:", final_path)