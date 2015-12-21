# Coool Code
import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    k=[int(i) for i in test.split()]
    s=set(k)
    d={}
    for i in s:
        d[i]=k.count(i)
    x=[int(i) for i in d.keys() if d[i]==1]
    print(k.index(min(x))+1 if x else 0)
