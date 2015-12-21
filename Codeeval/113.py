import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    l1, l2=test.split('|')
    l1=[int(i) for i in l1.split()]
    l2=[int(i) for i in l2.split()]
    res=[0 for i in l1]
    for i in range(len(l1)):
        res[i]=l1[i]*l2[i]
    print(' '.join(str(i) for i in res))
