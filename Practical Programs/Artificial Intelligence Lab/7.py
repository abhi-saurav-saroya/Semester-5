class Node:
    def __init__(self, name: str, is_max: bool, value: int = None, children: list = None) -> None:
        self.name = name
        self.is_max = is_max
        self.value = value
        self.children = children or []


def minimax(node, depth=0) -> float:
    indent = "  " * depth
    role = "MAX" if node.is_max else "MIN"

    if not node.children:
        print(f"{indent}Leaf: {node.name} | Value: {node.value}")
        return node.value

    print(f"{indent}[{role}] Node: {node.name}")

    if node.is_max:
        best_val = float('-inf')
        for child in node.children:
            child_val = minimax(child, depth + 1)
            best_val = max(best_val, child_val)

        node.value = best_val
        print(f"{indent}Result: {node.name} = {node.value}")

    else:
        best_val = float('inf')
        for child in node.children:
            child_val = minimax(child, depth + 1)
            best_val = min(best_val, child_val)

        node.value = best_val
        print(f"{indent}Result: {node.name} = {node.value}")
        
    return best_val


# A = Node("A", is_max=True, value=11)
# B = Node("B", is_max=True, value=70)
# C = Node("C", is_max=True, value=48)
# D = Node("D", is_max=True, value=54)
# E = Node("E", is_max=True, value=88)
# F = Node("F", is_max=True, value=53)
# G = Node("G", is_max=True, value=74)
# H = Node("H", is_max=True, value=94)
# I = Node("I", is_max=True, value=25)
# J = Node("J", is_max=True, value=23)
# K = Node("K", is_max=True, value=30)
# L = Node("L", is_max=True, value=41)
# M = Node("M", is_max=True, value=59)
# N = Node("N", is_max=True, value=50)
# O = Node("P", is_max=True, value=90)
# P = Node("P", is_max=True, value=45)

# depth3_node1 = Node("L31", is_max=False, children=[A, B])
# depth3_node2 = Node("L32", is_max=False, children=[C, D])
# depth3_node3 = Node("L33", is_max=False, children=[E, F])
# depth3_node4 = Node("L34", is_max=False, children=[G, H])
# depth3_node5 = Node("L35", is_max=False, children=[I, J])
# depth3_node6 = Node("L36", is_max=False, children=[K, L])
# depth3_node7 = Node("L37", is_max=False, children=[M, N])
# depth3_node8 = Node("L38", is_max=False, children=[O, P])

# depth2_node1 = Node("L21", is_max=True, children=[depth3_node1, depth3_node2])
# depth2_node2 = Node("L22", is_max=True, children=[depth3_node3, depth3_node4])
# depth2_node3 = Node("L23", is_max=True, children=[depth3_node5, depth3_node6])
# depth2_node4 = Node("L24", is_max=True, children=[depth3_node7, depth3_node8])

# depth1_node1 = Node("L11", is_max=False, children=[depth2_node1, depth2_node2])
# depth1_node2 = Node("L12", is_max=False, children=[depth2_node3, depth2_node4])

# root = Node("Root", is_max=True, children=[depth1_node1, depth1_node2])


values = [11, 70, 48, 54, 88, 53, 74, 94,
          25, 23, 30, 41, 59, 50, 90, 45]

leaves = [
    Node(chr(65 + i), True, value)
    for i, value in enumerate(values)
]

depth3 = [
    Node(f"L3.{i+1}", False, children=leaves[j:j+2])
    for i, j in enumerate(range(0, 16, 2))
]

depth2 = [
    Node(f"L2.{i+1}", True, children=depth3[j:j+2])
    for i, j in enumerate(range(0, 8, 2))
]

depth1 = [
    Node(f"L1.{i+1}", False, children=depth2[j:j+2])
    for i, j in enumerate(range(0, 4, 2))
]

root = Node("Root", True, children=depth1)


print("--- Starting Minimax Bottom-Up Backup Process ---")
final_score = minimax(root)
print("-------------------------------------------------")
print(f"The Minimax decision at Root is to choose Node A with a guaranteed payoff of: {final_score}")