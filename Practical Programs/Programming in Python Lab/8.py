num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Method 1: Using if-elif-else
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest number using if-else:", largest)

# Method 2: Using max() function
largest = max(num1, num2, num3)
print("Largest number using max():", largest)