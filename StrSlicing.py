mystr = "Focussed on Brand building and Public relations and marketing efforts"
print(len(mystr))#Print no of character in mystr
print(mystr[0:6])#Print First 5 character of mystr
print(mystr[0:6:2])#Print alternate characters from start upto 5th character
print(mystr[0:])#blank after : will automatically take the no of length of mystr
print(mystr[:6])# Blank before : will take the value 0 by default
print(mystr[ : :])# By default it take 0:Full lrngth:1
print(mystr[ : :2])# skip one alternate char from mystr
print(mystr[ : :-1])# Negative index rad char from the end
print(mystr.isalnum())# check wheathe mystr is alpha numeric
print(mystr.endswith("efforts"))#check wether mystr ends with "efforts"
print(mystr.count("e"))#count no of "e" in mystr
print(mystr.upper())# change entire string to upper case
print(mystr.lower())#change entire string to lower case
print(mystr.replace("on" , "at"))#Replace "on" with "at"