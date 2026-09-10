# Function to check whether a number is prime
def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# Printing prime numbers less than 20
print("Prime numbers less than 20:")

for num in range(2, 20):
    if is_prime(num):
        print(num, end=" ")