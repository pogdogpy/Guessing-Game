import time
import random

sel = input("Welcome to my number guessing game would you like to guess (a) 1-10 (b) 1-100 ")

if sel == "a":
    num1 = random.randint(1, 10)
    ans1 = int(input("Pick a number 1-10 "))
    if ans1 == num1:
        print("You Guessed Right!")
        time.sleep(3)
        quit()
    else:
        print("YOU GUESSED WRONG, Try Again!")
        print("Your Number was"), print(num1)
        time.sleep(3)
        quit()
        

if sel == "b":
    num2 = random.randint(1, 100)
    ans2 = int(input("Guess a number 1-100 "))
    if ans2 == num2:
        print("Holy Hell You Got it right?!?!?")
        time.sleep(3)
        quit()
    else:
        print("WRONG")
        print("Your Number Was"), print(num2)
        time.sleep(2)
        quit()


#made by pogdog#1372

