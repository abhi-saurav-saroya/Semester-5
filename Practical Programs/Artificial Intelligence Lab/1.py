import numpy as np


class Node:
    def __init__(self, value: str):
        self.value = value
        self.neighbors: list[Node] = []

    def __repr__(self):
        return self.value


def move_gen(node: Node) -> list[Node]:
    return node.neighbors


def goal_test(node: Node, goal: Node) -> bool:
    return node == goal


def simple_search(start: Node, goal: Node) -> tuple[bool, list[Node]]:
    open = np.array([start], dtype=object)
    closed = np.array([], dtype=object)

    while len(open) > 0:

        node = open[0]
        open = open[1:]

        closed = np.append(closed, node)

        if goal_test(node, goal):
            return True, closed.tolist()

        neighbors = move_gen(node)

        for neighbor in neighbors:
            if neighbor not in closed and neighbor not in open:
                open = np.append(open, neighbor)

    return False, closed.tolist()


if __name__ == "__main__":
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")

    a.neighbors.extend([b, c])
    b.neighbors.extend([a, c, d])
    c.neighbors.extend([a, b, d])
    d.neighbors.extend([c, b])

    status, path = simple_search(a, d)

    print("Search Result:")
    print("\tStart :", a)
    print("\tGoal :", d)
    print("\tGoal Found :", status)
    print("\tVisited:", " -> ".join(str(node) for node in path))