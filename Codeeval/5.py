#find Cycle Length
import sys

with open(sys.argv[1], 'r') as input:
    line_list = input.read().strip().splitlines()

for line in line_list:
    line=[int(i) for i in line.split()]

    #Check
    x,y=0,1
    length=len(line)
    while line[x]!=line[y]:
        x=(x+1)%length
        y=(y+2)%length
    #Length B/w 2
    begin=0
    x,y=0,abs(y-x)
    while line[x]!=line[y]:
        x=(x+1)%length
        y=(y+1)%length
        begin=begin+1
    #find cycle len
    dist,y=1,x+1
    while line[x]!=line[y]:
        y+=1
        dist=dist+1
    print(' '.join([str(i) for i in line[begin:begin+dist]]))
        
