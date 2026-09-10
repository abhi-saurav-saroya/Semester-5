class Power:
    # Constructor to initialize x and n
    def __init__(self, x: int, n: int):
        self.x = x
        self.n = n

    def pow(self) -> int:
        return self.x ** self.n


x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

# Creating an object of Power class
p = Power(x, n)
print(f"pow({x}, {n}) =", p.pow())