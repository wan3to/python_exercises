word = "pynative"
even_char = word[0::2]

for char in even_char:
    print(char)

word = input("Enter a word: ")
print("Original String:", word)

size = len(word)

print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])
    