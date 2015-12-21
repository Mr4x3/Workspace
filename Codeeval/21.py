def sum_d(d):
    k=[int(i) for i in str(d)]
    z=sum(k)
    return z

import sys
    
with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    print(sum_d(test))
