def remove_chars(word, n):
    print("Original String:", word)
    res = word[n:]
    return res

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
