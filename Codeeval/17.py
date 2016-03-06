#!/usr/bin/python3

import sys

def process(i):
    pass

with open(sys.argv[1], 'r') as input:
    line_list = input.read().strip().splitlines()

for line in line_list:
    l=[int(i) for i in line.split(',')]
    msum=sum(l[0:1])
    for i in range(len(l)):
        for j in range(i+1,len(l)+1):
            newsum=sum(l[i:j])
            msum=newsum if newsum>msum else msum
    print(msum)
