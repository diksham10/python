import random

x=random.randint(1,100)
while True:
    num=int(input("enter a number"))
    if num<x:
        print("number is higher")
    elif num>x:
        print("number is lower")
    else:
        print("you win")
        break
