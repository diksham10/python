# #Defining a simple factorial function:
# def factorial(x):
#     if x==0:
#         return 1
#     else:
#         return x*factorial(x-1)
# print(factorial(9)) 

#defining sum upto a given number without recursion with default parameter:
# def add(x=9):
#     result=0
#     for i in range(x+1):
#         result=result+i
#     print(result)
# add()

# #Keyword arguement : for postitonal order matters but for keyword it doesnot matter can be to neglet the order:
# def greet(name,age):
#     age+=1
#     print(f"hi {name} you will be {age} next year")
# greet("kisham",16)
# try:
#     greet(16,"kisham")
# except:
#     print("order ma hal fucchey")
# finally:
#     print("check")
# greet(age=23,name="kisham")    

# #Double value return:
# def add_diff(a,b):
#     add=a+b
#     if(a>b):
#         diff=a-b
#     elif(b>a):
#         diff=b-a
#     else:
#         diff=a-b
#     return add,diff
# jod,ghatau=add_diff(5,7)
# print(jod)
# print(ghatau)

# # *args **kwargs for function :

# def name(*args):
#     msg=[]
#     num=[]
#     for i in args:
#         if type(i)==str:
#             msg.append(i)
#         elif type(i)==int:
#             num.append(i)
#     print(msg,num)
# name('kisham',1,"diksham",2,"ayush",3,True)
# def names(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
        

# names(name="kisham",age=16,sex="male")



        