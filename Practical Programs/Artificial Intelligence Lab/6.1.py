MOVE_GEN = {
    'S': ['C', 'H', 'J', 'M'],
    'A': ['B', 'C', 'D'],
    'B': ['A', 'F'],
    'C': ['A', 'D', 'H', 'S'],
    'D': ['A', 'C', 'F', 'H'],
    'E': ['I', 'K'],
    'F': ['B', 'D', 'H', 'L'],
    'G': ['L', 'N', 'Q', 'R'],
    'H': ['C', 'D', 'F', 'M', 'S'],
    'I': ['E', 'J', 'K'],
    'J': ['I', 'K', 'O', 'P', 'S'],
    'K': ['E', 'I', 'J', 'P'],
    'L': ['F', 'G', 'N'],
    'M': ['H', 'O', 'S'],
    'N': ['G', 'L', 'Q'],
    'O': ['J', 'M', 'P', 'R'],
    'P': ['J', 'K', 'O'],
    'Q': ['G', 'N', 'R'],
    'R': ['G', 'O', 'Q']
}


def goal_test(node):
    return node == 'G'

def move_gen(node):
    return MOVE_GEN.get(node, [])

def occurs_in(node, node_pairs):
    for pair in node_pairs:
        if pair[0] == node:
            return True
    return False

def reconstruct_path(parent, goal):
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path


def db_dfs(start, depth_bound):
    OPEN = [(start, None, 0)]
    CLOSED = set()
    parent = {start: None}

    while OPEN:
        node, node_parent, depth = OPEN.pop(0)

        if goal_test(node):
            path = reconstruct_path(parent, node)
            return path, CLOSED, depth

        CLOSED.add(node)

        if depth < depth_bound:
            children = move_gen(node)
            new_nodes = []

            for child in children:
                if (not occurs_in(child, OPEN) and child not in CLOSED):
                    new_nodes.append(child)
                    parent[child] = node

            new_pairs = []
            for child in new_nodes:
                new_pairs.append((child, node, depth + 1))

            OPEN = new_pairs + OPEN

    return None, CLOSED, None


start = 'S'
depth_bound = int(input("Enter depth bound: "))
path, closed, depth = db_dfs(start, depth_bound)
print("\nCLOSED:", list(closed))

if path is not None:
    print("Goal found!")
    print("Path:", " -> ".join(path))
    print("Depth:", depth)
else:
    print("Goal not found within depth bound.")