# Importing a specific function from the module
from calculator import multiply

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the imported function
result = multiply(num1, num2)
print("Product:", result)