
import csv

with open("output.csv","r+") as file:
    reader=csv.reader(file)
    for i in reader:
        print(i)
    
    writer=csv.writer(file)
    writer.writerow(["kaluwa",12,"m"])

    file.seek(0)
    r=csv.DictReader(file)
    for row in r:
        print(row["Name"],row["Age"],row["sex"])
## the differnce between reader and dict reader is reader gives alll along with header in alist and another gives rows only 