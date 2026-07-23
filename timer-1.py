import time

again = "Y"
while again == "Y":
    while True:
        try:
            sec = int(input("How many seconds?: "))
            if sec > 0:
                break
            else:
                print("Can't enter negative numbers or zero")
        except:
            print("Characters and letters are invalid")

    for i in range(sec, 0, -1):
        print(i)
        time.sleep(1)

    print("Time is up")
    again = input("Do you want to go again?(Y/N): ").upper()
    while True:
        if again == "Y" or again == "N":
            break
        else:
            again = input("Enter a valid choice(Y/N): ").upper()

print("Have a good day!")
