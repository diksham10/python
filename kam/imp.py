import mymodule
import numpy as np
import pandas as pd
import csv

mymodule.greet("SULU")

# array=np.array([1,2,3])
# arr=np.arange(1,40,2).reshape(5,4)
# print(arr)

# lis=[1,2,3,4,5,6]
# tup=1,2,3,4,5
# set={1,1,2,3,6,6,4,3,5,5}
# dic={"name":"raj","id":3,"age":21,"sex":"Male"}

# a=pd.Series(lis)
# b=pd.Series(tup)
# c=pd.Series(dic)
# # d=pd.Series(set) #cant do with set cause its unordered
# print(a)
# print(b)
# print(c)
# # print(d)

#lsit of dictionaries:
x=[
    {
        "name": "Alice",
        "age": 28,
        "sex": "Female",
        "email": "alice@example.com",
        "city": "New York",
        "occupation": "Software Engineer"
    },
    {
        "name": "Bob",
        "age": 34,
        "sex": "Male",
        "email": "bob@example.com",
        "city": "Los Angeles",
        "occupation": "Data Analyst"
    },
    {
        "name": "Charlie",
        "age": 22,
        "sex": "Male",
        "email": "charlie@example.com",
        "city": "Chicago",
        "occupation": "Graphic Designer"
    },
    {
        "name": "Diana",
        "age": 30,
        "sex": "Female",
        "email": "diana@example.com",
        "city": "San Francisco",
        "occupation": "Product Manager"
    },
    {
        "name": "Ethan",
        "age": 26,
        "sex": "Male",
        "email": "ethan@example.com",
        "city": "Seattle",
        "occupation": "Marketing Specialist"
    }
]

y=pd.DataFrame(x)
# print(y)
y.to_csv("/home/dick_endra/python/output.csv",index=False)
z=pd.read_csv("/home/dick_endra/python/output.csv")
print(z)
x=pd.read_json("/home/dick_endra/python/sample_data.json")
print(x)