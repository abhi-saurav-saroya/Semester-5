import math
import heapq

def calculate_heuristics(coords: dict, goal: str = 'G', method: str ='manhattan') -> dict:
    gx, gy = coords[goal]
    h = {}

    for node, (x, y) in coords.items():
        if method == 'manhattan':
            h[node] = abs(x - gx) + abs(y - gy)
        elif method == 'euclidean':
            h[node] = round(math.sqrt((x - gx) ** 2 + (y - gy) ** 2), 2)
    return h


def weighted_a_star(graph: dict, h_manhattan: dict, start: str, goal: str, weight: float):
    open = []
    visited = set()

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    parent = {start: None}

    initial_f = g_score[start] + weight * h_manhattan[start]
    heapq.heappush(open, (initial_f, start))

    while open:
        current_f, current = heapq.heappop(open)

        if current in visited:
            continue

        if current == goal:
            path = []
            node = current

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            return path, g_score[goal]

        visited.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor in visited:
                continue

            tentative_g = g_score[current] + cost
            h = h_manhattan[neighbor]
            f = tentative_g + weight * h

            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                parent[neighbor] = current

                heapq.heappush(open, (f, neighbor))

    return list(visited), None


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

    print("\nMANHATTAN DISTANCE HEURISTICS")
    print("-" * 70)

    for node, value in sorted(h_manhattan.items()):
        print(f"h({node}) = {value}")

    weights = [1, 2, 3, 5]
    
    print("TEST CASES")
    print("-" * 70)

    for weight in weights:
        path, cost = weighted_a_star(graph, h_manhattan, 'S', 'G', weight)

        print(f"\nWeight = {weight}")
        print("-" * 70)

        if cost is not None:
            print(f"Path       : {' -> '.join(path)}")
            print(f"Total Cost : {cost}")
        else:
            print(f"Visited    : {' -> '.join(path)}")
            print("Total Cost : Goal not reached")
