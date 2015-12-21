def fibonacci(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        y=fibonacci(x-1)+fibonacci(x-2)
        return y

import sys
    
with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    x=int(test)
    print(fibonacci(x))
