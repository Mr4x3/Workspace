import sys



with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    x,y=[int(i) for i in test.split(',')]
    print(x-(x//y)*y)
