from abc import ABC , abstractmethod

class atm(ABC):
    def deposit(self):
        pass

class globalime(atm):
    #lets make and decorator
    def greet(fx):
        def mfx(*args,**kwargs):
            fx(*args,**kwargs)
            print("Thanks for using our service")
        return mfx
    amount=0
    def deposit(self,amnt):
        self.amount +=amnt
        print(f"New amount:{self.amount}")
    @greet
    def withdraw(self,amnt):
        print(f"amount withdrawn:{amnt}")
        self.amount -= amnt
        print(f"New balance= {self.amount}")    


obj=globalime()
obj.deposit(int(input("enter amount to be deposited:")))


try:
    def ask():
        x=input("do you want to withdraw ?(y/n):").lower().strip()
        if x=="y":
            obj.withdraw(int(input("Enter the amount to be withdraw:")))
        elif x=="n":
            print("okay")  
        else:
            print("Choose (y/n)") 
            ask()
            
except :
    print("some error occured")
ask()
    

    