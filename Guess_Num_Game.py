print("Guessing number game")

difficulty = int(input("1.easy 2.normal 3.hard 4.oneshot: "))

if difficulty == 1:
    import random

    random_number = random.choice(range(0,50))

    i = 1
    while i <= 10:
        guess = int(input(f"{i}-Take a guess: "))
        if guess == random_number:
            print("YOU WON!")
            break
        else:
            if guess < random_number:
                print("so low!")
            else:
                print("so high!")
            if i < 10:
                print("try again!")
            elif i <= 10:
                print("last shot!")
        i += 1
    else:
        print("YOU LOST!")
        print(f"The number was: {random_number}")

if difficulty == 2:
    import random

    random_number = random.choice(range(0,100))

    i = 1
    while i <= 5:
        guess = int(input(f"{i}-Take a guess: "))
        if guess == random_number:
            print("YOU WON!")
            break
        else:
            if guess < random_number:
                print("so low!")
            else:
                print("so high!")
            if i < 5:
                print("try again!")
            elif i <= 5:
                print("last shot!")
        i += 1
    else:
        print("YOU LOST!")
        print(f"The number was: {random_number}")

if difficulty == 3:
    import random

    random_number = random.choice(range(0,100))

    i = 1
    while i <= 3:
        guess = int(input(f"{i}-Take a guess: "))
        if guess == random_number:
            print("YOU WON!")
            break
        else:
            if i < 3:
                print("try again!")
            elif i <= 3:
                print("last shot!")
        i += 1
    else:
        print("YOU LOST!")
        print(f"The number was: {random_number}")

if difficulty == 4:
    import random

    random_number = random.choice(range(0,100))

    i = 1
    while i <= 1:
        guess = int(input(f"{i}-Take a guess: "))
        if guess == random_number:
            print("YOU WON!")
            break
        i += 1
    else:
        print("YOU LOST!")
        print(f"The number was: {random_number}")

print("thank you for playing!")
print("game is finished!")
