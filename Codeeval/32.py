#!/usr/bin/python3

import sys

def process(i):
    pass

with open(sys.argv[1], 'r') as input:
    line_list = input.read().strip().splitlines()

for line in line_list:
    r,t=line.split(',')
    #x,y=r.split()
    if r.endswith(t):
        print(1)
    else:
        print(0)
