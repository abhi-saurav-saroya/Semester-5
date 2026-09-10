from collections import deque

GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}


def breadth_first_search(start: str, goal: str) -> tuple[bool, list[str]]:
    queue = deque([start])
    visited = {start}
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        if node == goal:
            return True, order

        for neighbor in GRAPH[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False, order


if __name__ == "__main__":
    status, path = breadth_first_search("A", "D")

    print("Search Result:")
    print("\tStart : A")
    print("\tGoal : D")
    print("\tGoal Found :", status)
    print("\tVisited:", " -> ".join(path))