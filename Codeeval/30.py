import sys

def inter(x,y):
    copy=[]
    for i in x:
        for j in y:
            if i==j:
                copy.append(j)

    return copy
                

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    r,t=test.split(';')
    r,t=[int(i) for i in r.split(',')], [int(i) for i in t.split(',')]
    c=[str(i) for i in inter(r,t)]
    print(','.join(c))
