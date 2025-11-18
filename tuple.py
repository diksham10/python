# creatiing a tuple PARANTHESIS OR NOT PYHTON CAN IDENTIY THE TUPLE
x=(1,2,3,4,5)
y='a','b','b','c'
z="single", #this is single tuple 

# #The basic operations on tuoples are indedxing slicing concatenation and repetation:
# #1)Indexing : used to select value of tuple of given index
# print(x[1],y[2])
# #2) slicing :to selesct certain items from the tuples:
# print(x[1:3])
# #3)Concatenations:join two tuples:
# print(x+y)
# # Repetation or multiply: for multiplying the amount of elements in the tuple:(ONLY FOR SINGLE TUPLES)
# print(z*3)

# #Functuons in tuples:
# print(x.count(2),y.count("b"))
# print (x.index(3),y.index("b"))# give the index of given vlaue

# #unpacking tuples can also be done with list :(* CAN BE USED FOR UNPAXING IN GROUP)
# a,*b,c=x
# print(a,b,c)

# #Looping through a tuple
# for i in x:
#     print (i)


print(len(x))

