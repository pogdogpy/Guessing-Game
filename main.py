import time
import random
import colorama
from colorama import Fore
sel = input(Fore.MAGENTA + "Welcome to my number guessing game would you like to guess (a) 1-10 (b) 1-100 ")


 if sel == "a":
    num1 = random.randint(1, 10)
    ans1 = int(input(Fore.RED+"Pick a number 1-10 ---> "))
    if ans1 == num1:
        print(Fore.LIGHTMAGENTA_EX+"You Guessed Right!")
    else:
        print(Fore.CYAN+"You guessed Wrong.")
        time.sleep(0.6)
        print("Your Number Was " + str(num1))
    
   
        

if sel == "b":
    num2 = random.randint(1, 100)
    ans2 = int(input(Fore.CYAN+"Guess a number 1-100 ---> "))
    if ans2 == num2:
        print(Fore.RED+"Holy Hell You Got it right?!?!?")
        time.sleep(3)
        quit()
    else:
        print(Fore.YELLOW+"WRONG")
        time.sleep(0.9)
        print(Fore.GREEN+"Your Number Was " +  str(num2))
        time.sleep(2)
        quit()

