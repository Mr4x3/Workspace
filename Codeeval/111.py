import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    t=[i for i in test.split()]
    l=['junk',0]
    for i in t:
        if len(i)>l[1]:
            l=[i,len(i)]
    print(l[0])
