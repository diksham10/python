#set is unordered no INDEXING ans no  DUPLICATE
s={} #this cant be done as it creates empty dictonary instesad do
s=set()
s={1,2,3,1,2,3,2,3,4,5,}
print(s)

#adding
s.add(10)
s.update({7,8})
print(s)
print (sum(s))
#operations
# s.clear()
# s.remove(1)
# s.discard(6)
# #the differnce is that remove generated error but discard doesnot if theers id no element
# s.pop()

#mathematical sets operations set comperhensions:

# a={x for x in range(10)}
# b={x for x in range (15) if x%2==0 }
# print (a,b)
# print(a|b)
# print(a&b)
# print(a^b)
# print(a-b)




# print(s)