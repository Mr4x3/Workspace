def word(x,y,z):
    sol=[]
    for i in range(1,z+1):
        
        if i%x==0:
            if i%y==0:
                s='FB'
                sol.append(s)
            else:
                s='F'
                sol.append(s)
        elif i%y==0:
            sol.append('B')
        else:
            sol.append(i)
    return sol

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    fizz, buzz, limit = (int(i) for i in test.split())
    z=word(fizz, buzz, limit)
    for i in z:
        print(i,end=' ')
    print('')
