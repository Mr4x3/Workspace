import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    k=test.split()
    print(' '.join(i[0].capitalize() + i[1:] for i in k))
