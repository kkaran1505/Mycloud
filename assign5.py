my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
new_str = 'Pack'

start = 0
i = 0
n=(len(my_str) - len(sub_str) + 1)
print(n)
while start < n :
    if my_str[start] == sub_str[i]:
        i += 1
        if i == len(sub_str):
            my_str = my_str[:start - i + 1] + new_str + my_str[start + 1:]
            break
    else:
        start -= i
        i = 0
    start += 1
else:
    print(sub_str + ' not found')

print(my_str)