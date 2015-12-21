import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    l=[]
    k=[int(i) for i in test.split()]
    count=1
    start=1
    prev=int
    for i in k:
        if prev==i:
            count=count+1
        elif start:
            start=0
        else:
            l.extend([count,prev])
            count=1
        prev=i
    l.extend([count,prev])
    print(' '.join([str(i) for i in l]))
