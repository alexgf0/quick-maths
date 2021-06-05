import random
import time

def select_modality():
    while True:
        print("a) 1 digit by 1 digit multiplication")
        print("b) 1 digit by 2 digit multiplication")
        print("c) 2 digit by 2 digit multiplication")
        print("q) exit")

        opt = input("> ")

        if (opt == "a"):
            return "1x1"
        elif opt == "b":
            return "1x2"
        elif opt == "c":
            return "2x2"
        elif opt == "q":
            return "quit"

        print('\033[2J\033[H Please enter a valid option:') 

def get_numbers(modality: str):
    if modality == "1x1":
        a = random.randint(1,9)
        b = random.randint(1,9)
        return a,b
    elif modality == "1x2":
        a = random.randint(1,9)
        b = random.randint(10,99)
        return a,b
    elif modality == "2x2":
        a = random.randint(10,99)
        b = random.randint(10,99)
        return a,b
    else:
        raise Exception("Bad input to get_numbers function.")

print(" Welcome to quick maths!")
print("  q to exit.")

print("\nWhich modality would you like to play?\n")

modality = select_modality()

while True:
    a, b = get_numbers(modality)

    print("\033[2J\033[Hthe first number is: ", a)
    time.sleep(1.5)

    print("\033[2J\033[Hthe second number is: ", b)
    time.sleep(1.5)
    print("\033[2J\033[H", end="")
    res = input("Result: ")

    if res == 'q':
        print("Bye!")
        break

    if int(res) == a*b:
        print("Correct!!!")
        play = input("Wanna keep playing? (Y/n): ")
        if play == "n":
            print("Bye!")
            break
    else:
        print("WRONG!")
        print("the answer was: ", a*b)
        time.sleep(1)
