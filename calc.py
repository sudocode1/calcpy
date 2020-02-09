import random
import sys
import os

print("calc by sudocode1")
print("https://github.com/sudocode1/calcpy")

query = input("What kind of operation would you like to do? [+/-] ")

if query == "+" :
    add_num1 = input("What is your first number of the operation? eg [HERE] + num ")
    add_num2 = input("What is your second number of the operation? eg num + [HERE] ")

    print("Your answer is ", add_num1+add_num2)
else :
    if query == "-" :
        sub_num1 = input("What is your first number of the operation? eg [HERE] - num ")
        sub_num2 = input("What is your second number of the operation? eg num - [HERE] ")

        print("Your answer is ", int(sub_num1) - int(sub_num2))
    else :
        print("Your query is invalid!")
