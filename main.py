"""Python Script Guessing Game"""

import time
import sys
import random

#sel = input("Welcome to my number guessing game would you like to guess (a) 1-10 (b) 1-100 ")

#if sel == "a":
#    num1 = random.randint(1, 10)
#    ans1 = int(input("Pick a number 1-10 "))
#    if ans1 == num1:
#        print("You Guessed Right!")
#        time.sleep(3)
#        quit()
#    else:
#        print("YOU GUESSED WRONG, Try Again!")
#        print("Your Number was"), print(num1)
#        time.sleep(3)
#        quit()


#if sel == "b":
#    num2 = random.randint(1, 100)
#    ans2 = int(input("Guess a number 1-100 "))
#    if ans2 == num2:
#        print("Holy Hell You Got it right?!?!?")
#        time.sleep(3)
#        quit()
#    else:
#        print("WRONG")
#        print("Your Number Was"), print(num2)
#        time.sleep(2)
#        quit()


#made by pogdog#1372

# K.Dot woke

class Main:
    """Main Class For Guessing Game
    """
    def __init__(self) -> None:
        """__init__ function
        """
        self.sel = input("Welcome to my number guessing game." +
                         "Would you like to guess (a) 1-10 (b) 1-100 ")
        sel_options = {
            "a": self.one_through_ten,
            "b": self.one_through_onehundred
        }
        pick = sel_options.get(self.sel.lower())
        if pick is not None:
            pick()
        else:
            print("Invalid option")
            time.sleep(3)
            Main()


    def one_through_ten(self) -> None:
        """Guessing Number 1 Through 10
        """
        num1 = random.randint(1, 10)
        ans1 = int(input("Pick a number 1-10 "))
        if ans1 == num1:
            print("You Guessed Right!")
            time.sleep(3)
            sys.exit(0)
        else:
            print("You Guessed Wrong, Try Again!")
            print("Your Number was -> " + str(num1))
            time.sleep(3)
            sys.exit(0)


    def one_through_onehundred(self) -> None:
        """Guessing Number 1 Through 100
        """
        num2 = random.randint(1, 100)
        ans2 = int(input("Guess a number 1-100 "))
        if num2 == ans2:
            print("Holy Hell You Got it right?!?!?")
            time.sleep(3)
            sys.exit(0)
        else:
            print("WRONG\nYour Number was -> " + str(num2))
            time.sleep(3)
            sys.exit(0)


if __name__ == '__main__':
    Main()
