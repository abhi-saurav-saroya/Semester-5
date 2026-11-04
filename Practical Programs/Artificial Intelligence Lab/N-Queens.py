def is_safe(board, row, col):
    for previous_row in range(row):
        previous_col = board[previous_row]

        # Check column and diagonal conflicts
        if previous_col == col:
            return False

        if abs(previous_col - col) == abs(previous_row - row):
            return False

    return True


def solve_n_queens(n):
    board = [-1] * n

    def place_queen(row):
        # All queens have been placed
        if row == n:
            return True

        # Try every column in the current row
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col

                # Place queen in the next row
                if place_queen(row + 1):
                    return True

                # Backtrack if no solution is found
                board[row] = -1

        return False

    if place_queen(0):
        return board

    return None


def display_board(board, n):
    print("\nSolution:")
    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main program
n = int(input("Enter the number of queens (N): "))

if n <= 0:
    print("Invalid input! N must be a positive integer.")
else:
    solution = solve_n_queens(n)
    if solution is not None:
        display_board(solution, n)
    else:
        print("No solution exists for N =", n)