my_str = "peter piper picked A peck of pickled peppers."
print(f"Input: {my_str}")
out = ""
sent = ""
for char in my_str:
    if char == " " or char == ".":
        sent = sent + " " + out
        out = ""
    else:
        out = char + out

print(f"Output:{sent}")