n = int(input("Enter the number of key-value pairs: "))

my_dict = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

print("\nOriginal dictionary:", my_dict)

# Accessing a value using a key
key = input("\nEnter a key to access its value: ")
if key in my_dict:
    print("Value:", my_dict[key])
else:
    print("Key not found")

# Adding a new key-value pair
key = input("\nEnter a new key: ")
value = input("Enter its value: ")
my_dict[key] = value
print("Dictionary after adding:", my_dict)

# Updating a value
key = input("\nEnter a key to update: ")
if key in my_dict:
    value = input("Enter the new value: ")
    my_dict.update({key: value})
    print("Dictionary after updating:", my_dict)
else:
    print("Key not found")

# Using get() method
key = input("\nEnter a key to use get(): ")
print("Value:", my_dict.get(key, "Key not found"))

# Displaying all keys
print("\nKeys:", my_dict.keys())

# Displaying all values
print("Values:", my_dict.values())

# Displaying all key-value pairs
print("Items:", my_dict.items())

# Checking whether a key exists
key = input("\nEnter a key to search: ")
if key in my_dict:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")

# Removing an element using pop()
key = input("\nEnter a key to remove using pop(): ")
if key in my_dict:
    removed_value = my_dict.pop(key)
    print("Removed value:", removed_value)
    print("Dictionary after pop():", my_dict)
else:
    print("Key not found")

# Removing the last key-value pair using popitem()
if my_dict:
    removed_item = my_dict.popitem()
    print("\nRemoved last item using popitem():", removed_item)
    print("Dictionary after popitem():", my_dict)
else:
    print("\nDictionary is empty")

# Creating a copy of the dictionary
dict_copy = my_dict.copy()
print("\nCopy of dictionary:", dict_copy)

# Creating a dictionary using fromkeys()
keys = input("\nEnter keys for fromkeys() separated by space: ").split()
default_value = input("Enter the common value: ")
new_dict = dict.fromkeys(keys, default_value)
print("Dictionary using fromkeys():", new_dict)

# Clearing the dictionary
my_dict.clear()
print("\nDictionary after clear():", my_dict)