#dataclass it makes a class that already ahs some magic function like init repr and eq
# from dataclasses import dataclass


# @dataclass
# class ayush:
#     name:str
#     age:int
# obj=ayush("chiku",16)
# print(obj.name,obj.age)

class animal:
    def __init__(self,age):
        self._age=age
    @property
    def age(self):
        return self.age
    @age.setter
    def age(self,value):
        try:
            if value <= 0:
                raise ValueError("Age must be greater than 0")
            else:
                self._age = value  # set internal variable
        except ValueError as e:
            print(e)
    def show(self):
        print(f"{self._age} is an attribute")
obj=animal(3)
print(obj._age)
obj.show()
obj._age= 0
obj._age=20
print(obj._age)