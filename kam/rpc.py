import random


def rcp():
        x=random.randint(1,3)
        if x==1:
            msg="scissor"
        if x==2:
            msg="paper"
        if x==3:
            msg="rock"
        user=(input("enter scissor paper rock")).lower().strip()
        if user=="scissor":
            val=1
        elif user=="paper":
            val=2
        elif user=="rock":
            val=3
        else:
            print("choose scissor paper rock")

        print(f"compueter={msg} you={user}")
        if val==1:
            if x==1:
                print("draw")
            elif x==2:
                print("lose")
            else:
                print("win")
        elif val==2:
            if x==1:
                print("lose")
            elif x==2:
                print("draw")
            else:
                print("win")
        else:
            if x==1:
                print("win")
            elif x==2:
                print("lose")
            else:
                print("draw")
rcp()



