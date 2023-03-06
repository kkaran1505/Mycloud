print("Enter your age")
age = int( input() )
if age>=7 and age<= 75 :
    if age<18:
        print("You cannot drive")
    elif age==18:
        print("You have to visit DTO office for Physical Verification")
    else:
        print("You can Drive")
else:
    print("You have entered invalid age")
