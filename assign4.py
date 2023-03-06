my_str = "Peter Piper Picked A Peck Of Pickled Peppers."
sub_str = "Pickled"

for i in range(0,len(my_str)):
    if my_str[i:i+len(sub_str)] == sub_str:
        print(i)