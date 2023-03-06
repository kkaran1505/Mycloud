my_str = "Peter Piper Picked A Peck Of Pickled Peppers."
words = []
word = ""
for char in my_str:
    if char == " " or char == ".":
        words.append(word)
        word = ""
    else:
        word += char

print(words)