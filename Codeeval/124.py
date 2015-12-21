import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    sol,distance=[],[]
    k=test.split(';')[:-1]
    for i in k:
        x,y=i.split(',')
        distance.append(int(y))
    l=sorted(distance)
    r=0
    for i in l:
        s=i-r
        sol.append(s)
        r=i
    print(','.join(str(i) for i in sol))
    
