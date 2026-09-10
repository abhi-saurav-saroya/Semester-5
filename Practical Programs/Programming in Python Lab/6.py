# Taking tuple elements as input from the user
my_tuple = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

print("Original tuple:", my_tuple)

# Accessing tuple elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing the tuple
print("Sliced tuple:", my_tuple[1:])

# Length of tuple
print("Length of tuple:", len(my_tuple))

# Counting occurrences of an element
element = int(input("Enter an element to count: "))
print("Number of occurrences:", my_tuple.count(element))

# Finding the index of an element
element = int(input("Enter an element to find its index: "))

if element in my_tuple:
    print("Index of element:", my_tuple.index(element))
else:
    print("Element not found in tuple")

# Repeating a tuple
n = int(input("Enter number of times to repeat the tuple: "))
print("Repeated tuple:", my_tuple * n)

# Finding maximum and minimum values
print("Maximum element:", max(my_tuple))
print("Minimum element:", min(my_tuple))

# Finding sum of tuple elements
print("Sum of elements:", sum(my_tuple))

# Converting tuple to list
tuple_list = list(my_tuple)
print("Tuple converted to list:", tuple_list)

# Concatenating two tuples
second_tuple = tuple(map(int, input("Enter elements for another tuple: ").split()))
combined_tuple = my_tuple + second_tuple
print("Concatenated tuple:", combined_tuple)