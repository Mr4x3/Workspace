import sys

with open(sys.argv[1], 'r') as input:
    line_list = input.read().strip().splitlines()

for line in line_list:
    x,z=line.split(', ')
    for i in z:
        x=x.replace(i,'')
    print(x)
