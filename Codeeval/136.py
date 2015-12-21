import sys
import collections

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()
print(list(enumerate(test_cases)))
