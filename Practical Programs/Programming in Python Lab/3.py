# Creating two strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = str1 + " " + str2              # Concatenating the strings
print("Concatenated string:", result)

# Accessing a substring using slicing
start = int(input("Enter the starting index of substring: "))
end = int(input("Enter the ending index of substring: "))

substring = result[start:end]
print("Substring:", substring)