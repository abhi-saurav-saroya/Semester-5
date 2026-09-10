import datetime

now = datetime.datetime.now()       # Get the current date and time

# Format and print the current date and time
print("Expected Output: ")
print(now.strftime("%a %b %d %H:%M:%S IST %Y"))