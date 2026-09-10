import os
import string

folder = os.path.dirname(os.path.abspath(__file__))

file_name = input("Enter the name of the text file: ")
file_path = os.path.join(folder, file_name)

with open(file_path, "r") as file:
    text = file.read()

# Remove punctuation from the text
text = text.translate(str.maketrans("", "", string.punctuation))

words = text.split()
unique_words = set(word.lower() for word in words)
sorted_words = sorted(unique_words)

print("Unique words in alphabetical order:")
for word in sorted_words:
    print(word, end=", ")