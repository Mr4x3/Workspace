#!/usr/local/bin/python3
import sys

with open(sys.argv[1], 'r') as input:
    line_list = input.read().strip().splitlines()
k=[]
for line in line_list:
    rt=line.split('=')
    pakg=rt[0]
    k.append(pakg)
with open('installed.txt','w') as f:
    for i in k:
        f.write(i)
        f.write('\n')
