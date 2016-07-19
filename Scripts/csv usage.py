import csv
import os
print(os.getcwd())
x=[]
with open('cat.csv') as csv2:
    d=csv.reader(csv2)
    for i in d:
        l=list(i)
        if d.index(i)==0:
            x.extend(i.insert(2, "catagory,subcatagory,subsubcatagory"))
        else:
            s=i[1].split('/')
            i.pop(1)
            if not len(i)==4:
                stuff="{},{},{},NA".format(s)
            else:
                stuff="{},{},{},NA".format(s)
            x.extend(i.insert(2, stuff))
            
