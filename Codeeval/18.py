import sys

def multi2(x,n):
    for i in range(x+1):
        if n*i>x:
            return n*i

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    x,n=test.split(',')
    x,n=int(x), int(n)
    print(multi2(x,n))
