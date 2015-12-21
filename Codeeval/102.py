import sys
import re

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    k=sum([int(i) for i in re.findall('id": (\d+), "label"',test)])
    print(k)
