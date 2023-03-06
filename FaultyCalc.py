def calculator():
    print("Welcome to Calculator")
    operation = input("""" Please type the maths operator you want to use:\n 
                      + for Addition \n 
                      - for Subtraction  \n 
                      * for Multiplication \n  
                      / for Division \n 
                      ** for power \n 
                      % for module \n 
                      Enter your Choice """)
    num1 = int(input("Enter First Number \n"))
    num2 = int(input("Enter Second Number \n"))
    if operation == '+':
        if num1 == 56 and num2 == 9:
            print("56+9=77")
        else:
            print(f"{num1}+{num2}={num1+num2}")
    elif operation == '*':
        if num1 == 45 and num2 == 3:
            print("45*3=555")
        else:
            print(f"{num1}*{num2}={num1*num2}")
    elif operation == '/':
        if num1 == 56 and num2 == 6:
            print("56/6=4")
        else:
            print(f"{num1}/{num2}={num1/num2}")
    elif operation == '**':
        print(f"{num1}**{num2}={num1**num2}")
    elif operation == '%':
        print(f"{num1}%{num2}={num1%num2}")
    else:
        print("You pressed an invalid key")

    again()

def again():
        cal_again= input("Do you want to calculate again. \n Type y for Yes and n for No ")

        if cal_again == 'y':
            calculator()
        elif cal_again == 'n':
            print("See you later")
        else:
            again()

calculator()
