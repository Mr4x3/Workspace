import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    i=int(test)
    if i%2==0:
        print(1)
    else:
        print(0)
    
