import random

choice = input("Choose the difficulty (easy/hard/ultimate): ").lower()

def game(choice):
    """A game which may cause your device to shut forever if played on other than my device."""

    #Choose the level you want to play at

    if choice == "easy":
        easy()

    elif choice == "hard":
        hard()

    elif choice == "ultimate":
        ultimate()

def again():
    """Asking the user if he wants to continue playing"""

    x = input("Do you wanna continue?\n").lower()

    if x == "yes":
        print("first solve this before next attempt.")
        will()

    else:
        print("Okay bye!")

def will():
    """A test for the ones who failed an attempt of the game but want to continue."""

    x1 = random.randint(1, 100
                        )
    y1 = random.randint(1, 100)

    ans = int(input(f"{x1}X{y1} = "))

    if ans == x1 * y1:
        print("Good, you can continue.")
        game(choice)
    else:
        print("Do maths first brother!")


def easy():
    """Easy level"""

    x = random.randint(1, 10)
    y = int(input("Enter your number: "))

    if y == x:
        print("\n" * 100)
        print("Lucky Day!")
        print("You were luck enough to get out of this circle.")
        print("Congratulations!")

    else:
        print("\n" * 100)
        print("Better luck next time!")
        again()

def hard():
    """Hard level"""

    x = random.randint(1, 50)
    y = int(input("Enter your number: "))

    if y == x:
        print("\n" * 100)
        print("Lucky Day!")
        print("You were luck enough to get out of this circle.")
        print("Congratulations!")

    else:
        print("\n" * 100)
        print("Better luck next time!")
        again()

def ultimate():
    """Ultimate level of difficulty"""

    x = random.randint(1, 100000)
    y = int(input("Enter your number: "))

    if y == x:
        print("\n" * 100)
        print("Lucky Day!")
        print("You were luck enough to get out of this circle.")
        print("Congratulations!")

    else:
        print("\n" * 100)
        print("Better luck next time!")
        again()

game(choice)
