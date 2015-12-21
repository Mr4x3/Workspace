import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    k=sorted(set([int(i) for i in test.split(',')]))
    print(','.join([str(i) for i in k]))
