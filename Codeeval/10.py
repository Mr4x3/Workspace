import sys

with open(sys.argv[1], 'r') as input:
    line_list = input.read().strip().splitlines()

for line in line_list:
    l=line.split()
    z=int(l.pop())
    if z>len(l):
        continue
    else:
        print(l[-z])
