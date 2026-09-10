class ReverseString:
    # Constructor to initialize the string
    def __init__(self, text):
        self.text = text

    # Function to reverse the string word by word
    def reverse(self):
        words = self.text.split()
        words.reverse()
        return " ".join(words)


text = input("Enter a string: ")

obj = ReverseString(text)
print("Reversed string:", obj.reverse())