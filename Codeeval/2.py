import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

y={}
s=1
for test in test_cases:
    if s==1:
        x=int(test)
        s=0
    else:
        y[len(test)]=test
sa=sorted(list(y.keys()))
for i in range(x):
    print(y.get(sa.pop()))
