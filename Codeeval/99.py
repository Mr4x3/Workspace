import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    l=[int(i) for i in test.replace('(','').replace(', ',' ').replace(') ',' ').replace(')','').split()]
    x=((l[0]-l[2])**2+(l[1]-l[3])**2)**.5
    print(int(x))
    
