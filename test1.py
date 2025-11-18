# #reverse string:
# msg="hello"
# rev=msg[::-1] #using slicing
# print(msg+"is reversed to "+rev)
# msgs='kill'
# i=''.join(reversed(msgs)) #using join and reverse
# print (i)

# #palindrome :
# msg="Non"
# msg=msg.lower()
# rev=msg[::-1]
# if msg == rev:
#     print("it is palindrome")
# else:
#     print("not palindrome")    

# #factorial of a number :
# # x=int(input("enter a number"))
# # factorial=1
# # for i in range(1,x+1):
# #     factorial=i*factorial
# # print(factorial)
# def fact(n):
#     return 1 if n==0 else n*fact(n-1)
# print(fact(5))

# #'check vowels:
# vowels="aeiou"
# x=0

# msg=input("enter a string")

# for char in msg:
#     if char in vowels:
#         x+=1
# print("is vowel so count="+str(x))

# #lamlbda function : to create a function in a single line :
# add=lambda x,y: (x**2) + (y**2)
# print(add(9,3))

# msg="hello world"
# x=list(msg)
# y=x[::-1]
# msg1="".join(y)
# print(msg,msg1)