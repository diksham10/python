# #creatting an empty list :
# bikes=[]
# #adding through a lsit and ading at a positiion
# bikes.append("ns200")
# bikes.append("zxr")
# #adding at an index
# bikes[0]="sikes" if  anyhthin at the position in the moment then it is replaced
# test=[]
# msg="happy"
# test.extend(msg)
# print(test)
# print(test[-1])
# L=["hi","hii","hiii"]
# RL=L[::-1]
# print(L+RL)
test=[1,2,3,4,5,6,7,8,9]
test1=["apple"]
test2=["apple","ball","cat","dog"]

# slicing and copying:
# msg=test2[:]
# print(msg)
# # del msg[1]
# msg.remove("ball")
# if "ball" in msg:
#     print(msg)
# else:
#     msg.insert(1,"ball")
#     print(msg)

# #popping an item :
# popped_item=test.pop(2)
# print(popped_item)

# #reverse a list and sorting a list :
# test2.sort(reverse=True)
# msg=test2[::-1]
# print(msg)
# print(len(msg))

# test2.insert(1,test1) #nested list ``
# print(test2)


# msg="hekko"
# msg=list(msg)
# print (msg)

#list comprehension: making alist in single line insread of appending using a loop

# numbers=[x for x in range (5) if x%2==0]
# print(numbers)
#testing the sum function
# x=sum(test)
# print(x)
# tup=2,
# square=list(tup)
# square_odd=[x**2 if x%2==0 else x**3 for x in range(10)]
# print(square_odd,square)

# print (test2)
# test2[0]="avacado"
# print (test2)





# alist=[s for s in range(1,6) if s%2==0  ]
# print(alist)
# s=[]
# for i in range(1,6):
#     if i%2==0:
#         s.append()

# adict={x:x**2 for x in range(0,20,2) }
# print(adict)

# atup=(s for s+(s-1) in range(0,300,50) )
# print(type(atup))

# x=1,
# print(x)

# generator :
def fibo(x):
    a,b=0,1
    while a<=4:
        yield a
        a,b=b,a+b
x=int(input("enter a number for fibonacci to be calculated"))
for j in fibo(x):
    print (j)

