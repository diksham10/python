name="king"
age=25

#f string:
print(f"1 hi {name} age:{age}")

#format:

print("2 hi {} age:{}".format(name,age))
#or:
print("3 hi {0} age:{1}".format(name,age))
#or
print("4 hi {n} age:{aa}".format(n=name,aa=age))

#  "%" same as c:
print("5 hi %s age:%d"%(name,age))

print("6 hi "+name+" age:"+str(age))

