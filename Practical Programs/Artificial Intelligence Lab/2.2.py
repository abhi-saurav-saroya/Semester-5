GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

def depth_first_search(start: str, goal: str) -> tuple[bool, list[str]]:
    stack = [start]
    visited = {start}
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        if node == goal:
            return True, order

        for neighbor in GRAPH[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return False, order



if __name__ == "__main__":
    status, path = depth_first_search("A", "D")

    print("Search Result:")
    print("\tStart : A")
    print("\tGoal : D")
    print("\tGoal Found :", status)
    print("\tVisited:", " -> ".join(path))