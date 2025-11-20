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

class bank:
    def __init__(self,user,balance,pwd):
        