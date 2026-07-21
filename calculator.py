choice = "y"
while choice == "y":
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    op = input("Choose an operator (+,-,*,/): ")

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("You cannot divide with zero")
        else:
            print(num1 / num2)
    else:
        print("Enter a proper operator")
    choice = input("Do you want to calculate again? (y/n) ")
    while choice != "y" and choice != "n":
        choice = input("Pick a valid choice: ")

print("Have a nice day")