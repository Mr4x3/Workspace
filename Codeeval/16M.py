#!/usr/bin/python3

import sys

def process(i):
    pass

with open(sys.argv[1], 'r') as input:
    line_list = input.read().strip().splitlines()

for line in line_list:
    num=int(line)
    k=str(bin(num))
    z=[int(i) for i in k[2:]]
    print(sum(z))
