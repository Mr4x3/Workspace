import sys

with open(sys.argv[1], 'r') as input:
    line_list = input.read().strip().splitlines()

for line in line_list:
    z=list(line)
    char=''
    for i in z:
        if line.count(i)==1:
            char=i
            break
    print(char)
