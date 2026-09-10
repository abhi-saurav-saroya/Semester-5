a = float(input("Enter the length of first side: "))
b = float(input("Enter the length of second side: "))
c = float(input("Enter the length of third side: "))

# Finding the largest side
largest = max(a, b, c)

# Checking the Pythagorean theorem
if largest == a:
    other1, other2 = b, c
elif largest == b:
    other1, other2 = a, c
else:
    other1, other2 = a, b

if a + b > c and a + c > b and b + c > a and largest ** 2 == other1 ** 2 + other2 ** 2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")