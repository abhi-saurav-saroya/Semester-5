# Taking list elements as input from the user
my_list = list(
    map(
        int, 
        input("Enter list elements separated by space: ").split()
    )
)
print("Original list:", my_list)

# Appending an element to the list
element = int(input("Enter an element to append: "))
my_list.append(element)
print("List after appending:", my_list)

# Removing an element from the list
element = int(input("Enter an element to remove: "))

if element in my_list:
    my_list.remove(element)
    print("List after removing:", my_list)
else:
    print("Element not found in the list")