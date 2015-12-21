import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    t=test.split()
    k=[t[i] for i in range(len(t)) if i%2]
    l=[t[i] for i in range(len(t)) if not i%2]
    x=''
    for i in range(len(k)):
        if l[i]=='00':
            x=x+k[i].replace('0','1')
        else:
            x=x+k[i]
    print(int(x,2))
