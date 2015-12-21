import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    l=[float(i) for i in test.split()]
    x=sorted(l)
    print(' '.join(['%.3f' %i for i in x]))
#   print(' '.join(['{:.3f}'.format(i) for i in x]))

