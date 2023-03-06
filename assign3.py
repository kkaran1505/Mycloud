text = 'peter piper picked a peck of pickled peppers.'
n = len(text)-1
i = 0
while i <= n:
    if text[i] == 'p':
        print(i)
    i += 1