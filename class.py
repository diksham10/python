# class dog:
#     def bark(self,name):
#         self.name=name
#         print(f"the dog {self.name} is barking")
# d = dog()
# d.bark("husky")
# this is a simle class that has an object d and it is uesd to call the function inside the class

# class car:
#     i=43
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#         print(brand,self.model,self.price,) #self use or no use no matter

# car1= car("honda","vdv",299900000)
# car2= car("bmw","killer",3213023206)

# class student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
#     def display(self):
#         print(f"student name={self.name} \nstudent grade={self.grade}")
# stu1=student("ayush",12)
# stu2=student("rochak",12)
# stu1.display()
# stu2.display()

#now lets use class method and static method:
# class rochak:
#     age=12

#     @classmethod
#     def display_age(cls):
#         print(f"the age of rochak is {cls.age}")
# r=rochak()
# r.display_age()
# class jod:
#     @staticmethod
#     def add(a,b):
#         print(f"the sum is {a+b}")
# j=jod()
# j.add(9,10)


# #some dunder functions :
# class hi:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return hi(self.x+other.x,self.y+other.y)
#     def __str__(self):
#         return f"({self.x},{self.y})"
# p1=hi(1,2)
# p2=hi(3,4)
# print(p1 + p2)

#now lets learn encapsulation:
#encapsulation is the process of hiding the confidential data from the users (access controll) 
#it differs from abstracton as it hides the data but abstraction hides the unnecessary info about a method:

# class bank:
#     __info={
#     "alice1": {"name": "Alice", "balance": 1200.50, "pwd": "alice123", "gender": "Female", "age": 25},
#     "bob2": {"name": "Bob", "balance": 950.75, "pwd": "bob456", "gender": "Male", "age": 30},
#     "charlie3": {"name": "Charlie", "balance": 500.00, "pwd": "charlie789", "gender": "Male", "age": 22},
#     "diana4": {"name": "Diana", "balance": 1500.20, "pwd": "diana321", "gender": "Female", "age": 28},
#     "edward5": {"name": "Edward", "balance": 800.00, "pwd": "edward654", "gender": "Male", "age": 35}
# }



#     def __init__(self,id,pwd):
#         self.id=id
#         self.__pwd=pwd
        
    
#     def display(self):
#         # x=self.info
#         # print(self.id,self.info)
#         try:
#             # user = self.info[self.id]
#             if(self.__info[self.id]["pwd"]== self.__pwd):
#                 print(self.__info[self.id]["name"],self.__info[self.id]["balance"],self.__info[self.id]["gender"],self.__info[self.id]["age"],self.__info[self.id]["name"])
#                 print('sdf')
                
#             else:
#                 print('fuck you imposter!!')
        
#         except Exception as e:
#             print("Some error occurred:", type(e))
    
#     def deposit(self,amount):
#         try:
#             self.__info[self.id]["balance"] +=amount
            
#             print(f"new balance:{self.__info[self.id]["balance"]}")
#         except:
#             print("failed")

        
    

# x=bank("charlie3","charlie789")
# x.deposit(500)
# x.display()
# print(bank.__info)
# import time
# # t=time.strftime("%H:%M:%S")
# # print(t)
# class zoo:
#     def feed(self,food,amt):
#         print(f"  ate {amt} {food}")
# class lion(zoo):
#     def feed(self,food,amt):
#         print(f"lion ate {amt} {food}")
#     def roar(self):
#         print("the lion roared it needs food")

# x=lion()
# h=time.strftime("%H")
# print(h)
# m=time.strftime("%M") 
# print(type(h))
# if(h=='12'):
#     print('---------------------------------')
#     x.roar()

# if(h==12 and m==25):
#     x.feed('meat','12kg')
    
# class gf1:
#     def dis(self):
#         print("i am gf 1")
# class gf2:
#     def dis1(self):
#         print(" i am gf 2")
# class kisham(gf1,gf2):
#     pass
#     # def dis(self):
#     #     pass
# obj=kisham()
# obj.dis()
# obj.dis1()

# using super to inherit the function form the parent class
# class A:
#     def show(self):
#         print("A show method")
#     def kiss(self):
#         print("a will kill b")

# class B(A):
#     def show(self):
#         super().show()
#         A.show(self)
#         super().kiss()
#         print("B show method")
# obj=B()
# obj.show()

#MRO====> method resolution order is the process of letting python know what to run when multiple parent are present:
class base:
    def xa(self):
        pass
class harami():
    def xa(self):
        print ("Lastai harami xa yarr")
        super().xa()
class sexy():
    def xa(self):
        print ("Lastai sexy pani xa")
        # super().xa()
        #ya super rakhera error aayoo kinaki ya super vayesi tesle aba last ma object call garxa jun ma xa()function nai xna

class nam(harami,sexy):
    def name(self,hah):
        self.hah=hah
        
        print(f"{self.hah} ta :")
        super().xa()

obj=nam()
obj.name("ayush")
# print (name.)
print(nam.mro())# the order is nam->harami ko xa()-> sexy ko xa()->object yedi sexy ma ni super vaye josle chain break garo so hatako
obj1=nam()
obj1.name("kisham")



        
