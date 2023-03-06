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
            print(f"{num1}+{num2}={num1+num2}")
    elif operation == '*':
            print(f"{num1}*{num2}={num1*num2}")
    elif operation == '/':
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