GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

DOMAINS = {
    "A": [1, 2, 3],
    "B": [1, 2, 3],
    "C": [1, 2, 3],
    "D": [1, 2, 3]
}

SOLUTION = {}


def constraint_satisfaction_problem() -> list[tuple[str, int]]:
    variables = list(DOMAINS)
    assignment = {}

    def is_valid(variable: str, value: int) -> bool:
        for neighbor in GRAPH[variable]:
            if neighbor not in assignment:
                continue

            if variable == "B" and neighbor == "D":
                if value >= assignment[neighbor]:
                    return False

            elif variable == "D" and neighbor == "B":
                if assignment[neighbor] >= value:
                    return False

            elif value == assignment[neighbor]:
                return False

        return True

    def backtrack(index: int) -> bool:
        if index == len(variables):
            return True

        variable = variables[index]

        for value in DOMAINS[variable]:
            if is_valid(variable, value):
                assignment[variable] = value

                if backtrack(index + 1):
                    return True

                del assignment[variable]

        return False

    if backtrack(0):
        SOLUTION.update(assignment)
        return list(SOLUTION.items())

    return []


if __name__ == "__main__":
    solution = constraint_satisfaction_problem()

    for variable, value in solution:
        print(f"{variable}: {value}")