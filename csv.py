
import csv

with open("/home/dick_endra/python/output.csv","r+") as file:
    reader=csv.reader(file)
    for i in reader:
        print(i)
    
    