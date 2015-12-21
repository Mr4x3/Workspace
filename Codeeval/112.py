import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    number, swap=test.split(':')
    number=[int(i) for i in number.split()]
    swap=[i for i in swap.split(',')]
    for i in swap:
        x,y=i.split('-')
        x,y=int(x), int(y)
        number[x], number[y]=number[y], number[x]
    print(' '.join([str(i) for i in number]))
