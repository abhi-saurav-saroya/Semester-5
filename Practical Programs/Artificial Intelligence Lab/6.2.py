# DFID (Depth-First Iterative Deepening)

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


def depth_limited_dfs(node, depth_limit, path):

    if goal_test(node):
        return path

    if depth_limit == 0:
        return None

    for child in move_gen(node):

        if child not in path:
            result = depth_limited_dfs(
                child, depth_limit - 1, path + [child]
            )

            if result is not None:
                return result

    return None


def dfid(start):

    for depth_bound in range(len(MOVE_GEN)):

        print("Searching with depth bound:", depth_bound)

        path = depth_limited_dfs(
            start, depth_bound, [start]
        )

        if path is not None:
            return path, depth_bound

    return None, None


# MAIN PROGRAM

start = 'S'

path, depth = dfid(start)

if path is not None:
    print("\nGoal found!")
    print("Path:", " -> ".join(path))
    print("Depth:", depth)
else:
    print("\nGoal not found.")