word = input("Enter a word: ")

reversed_word = ""
#concatenates each character to the start of the new string
for char in word:
    reversed_word = char + reversed_word

print("Reversed word:", reversed_word)
