import random

choice = "y"
while choice == "y":
    rand = random.randint(0, 100)
    guess = int(input("Guess the number: "))
    count = 1

    while rand != guess:
        if rand > guess:
            guess = int(input("Guess higher: "))
            count += 1
        elif rand < guess:
            guess = int(input("Guess lower: "))
            count += 1
        if count > 7:
            break

    if count <= 7:
        print("Correct answer!")
        count = str(count)
        print("Number of attempts: " + count)
    else:
        print("You ran out of attempts")

    choice = input("Do you want to play again? (y/n) ")

print("Thanks for playing!")