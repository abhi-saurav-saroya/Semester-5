import os
folder = os.path.dirname(os.path.abspath(__file__))

# Taking file names from the user
source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

# Creating the complete file paths
source_path = os.path.join(folder, source_file)
destination_path = os.path.join(folder, destination_file)

# Opening the source file in read mode
with open(source_path, "r") as file1:
    content = file1.read()

# Opening the destination file in write mode
with open(destination_path, "w") as file2:
    file2.write(content)

print("Contents copied successfully.")