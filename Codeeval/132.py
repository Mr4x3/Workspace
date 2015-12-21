import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    k=test.split(',')
    t=set(k)
    for i in t:
        if k.count(i)>len(k)/2:
            TME=i
            break
        else:
            TME='None'
    print(TME)
