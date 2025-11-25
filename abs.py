from abc import ABC ,abstractmethod
import time
print(time.strftime("%H:%M:%S"))
h=time.strftime("%H")
m=time.strftime("%M")
class zooAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def eat(self):
        pass
    def die(self):
        print("it died ")
class lion(zooAnimal):
    def __init__(self,food,amt):
        self.food=food
        self.amt=amt
        
    def speak(self):
        print("lion roared")
    def eat(self):
        print(f"lion ate {self.food} {self.amt}")
        # super().die()
class tiger(zooAnimal):
    def __init__(self,food,amt):
        self.food=food
        self.amt=amt
        
    def speak(self):
        print("tiger roared")
    def eat(self): 
        print(f"tiger ate {self.food} {self.amt}")
       

obj1=lion("meat","5kg")
obj2=tiger("meat","4kg")
obj=[obj1,obj2]

for a in obj:
   
    if h<"13" :
        a.speak()
    elif h>'3':
        print("it died")
    else:
        a.eat()









        

    

    