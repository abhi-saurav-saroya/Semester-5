import math
import heapq

def calculate_heuristics(coords: dict, goal:str = 'G', method:str ='manhattan') -> dict:
    gx, gy = coords[goal]
    h = {}

    for node, (x, y) in coords.items():
        if method == 'manhattan':
            h[node] = abs(x - gx) + abs(y - gy)
        elif method == 'euclidean':
            h[node] = round(math.sqrt((x - gx) ** 2 + (y - gy) ** 2), 2)
    return h


def a_star(graph: dict, h_manhattan: dict, start: str, goal: str):
    open = []
    visited = set()

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    parent = {start: None}

    step = 0

    heapq.heappush(open, (g_score[start] + h_manhattan[start], start))

    print("\n" + "=" * 65)
    print("                 A* SEARCH ALGORITHM")
    print("=" * 65)

    while open:
        step += 1

        print(f"\n{'─' * 65}")
        print(f"STEP {step}")
        print(f"{'─' * 65}")

        print("\nOPEN LIST:")
        for f, node in sorted(open):
            g = g_score[node]
            h = h_manhattan[node]
            print(
                f"  Node {node}: "
                f"g(n) = {g}, "
                f"h(n) = {h}, "
                f"f(n) = {f}"
            )

        current_f, current = heapq.heappop(open)

        current_g = g_score[current]
        current_h = h_manhattan[current]
        current_f = current_g + current_h

        print("\nSELECTED NODE:")
        print(
            f"  {current} "
            f"(g = {current_g}, "
            f"h = {current_h}, "
            f"f = {current_f})"
        )
        
        if current in visited:
            print("  Status: SKIPPED (already visited)")
            continue

        if current == goal:
            print("\nGOAL REACHED!")
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            print("\nFINAL PATH:")
            print(" -> ".join(path))
            print(f"TOTAL PATH COST: {g_score[goal]}")
            print("=" * 65)
            return

        visited.add(current)
        print("\nVISITED NODES:")
        print("  ", visited)

        print(f"\nEXPLORING NEIGHBORS OF {current}:")
        for neighbor, cost in graph[current].items():
            print(f"\n  Neighbor: {neighbor}")
            print(f"  Edge cost: {cost}")

            if neighbor in visited:
                print("  Status: SKIPPED (already visited)")
                continue

            tentative_g = g_score[current] + cost
            h = h_manhattan[neighbor]
            f = tentative_g + h

            print(f"  Tentative g(n): {tentative_g}")
            print(f"  Heuristic h(n): {h}")
            print(f"  Calculated f(n): {f}")

            if tentative_g < g_score[neighbor]:
                print("  Status: UPDATED (cheaper path found)")
                g_score[neighbor] = tentative_g
                parent[neighbor] = current
                heapq.heappush(open, (f, neighbor))
                print("  Added to OPEN list.")

            else:
                print("  Status: SKIPPED (no cheaper path)")

    print("\nNO PATH FOUND.")


if __name__ == "__main__":
    graph = {
        'A': {'C': 6 , 'G': 6},
        'B': {'C': 6, 'G': 10, 'D': 20, 'F': 14},
        'C': {'A': 6, 'B': 6, 'F': 10, 'G': 14},
        'D': {'B': 20, 'E': 8, 'F': 8, 'S': 20},
        'E': {'S': 8, 'F': 12, 'D': 8},
        'F': {'B': 14, 'C': 10, 'D': 8, 'E': 12},
        'G': {'A': 6, 'B': 10, 'C': 14},
        'S': {'E': 8, 'D': 20}
    }

    coords = {
        'A': (0, 1),
        'B': (5, 3),
        'C': (1, 4),
        'D': (8, 6),
        'E': (13, 8),
        'F': (4, 9),
        'G': (3, 0),
        'S': (12, 2),
    }

    h_manhattan = calculate_heuristics(coords)

    print("Calculated Manhattan Distance Heuristics h(n):")
    for node, val in sorted(h_manhattan.items()):
        print(f"  Node {node}: h({node}) = {val}")

    a_star(graph, h_manhattan, 'S', 'G')