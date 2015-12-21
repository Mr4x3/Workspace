import sys

with open(sys.argv[1], 'r') as input:
    line_list = input.read().strip().splitlines()

for line in line_list:
    t=[int(i) for i in line.split()]
    t2=t[-1::-2]
    print(' '.join([str(i) for i in list(t2)]))
