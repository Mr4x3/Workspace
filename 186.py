#!/usr/local/bin/python3
import sys

with open(sys.argv[1], 'r') as input:
    line_list = input.read().strip().splitlines()

for line in line_list:
    days, values = line.split(';')
    days=int(days)
    values=[int(i) for i in values.split()]
    sumx=int()
    z=len(values)-days
    for i in range(z+1):
        s=sum(values[i:i+days])
        if sumx<s:
            sumx=s
    print(sumx)
