import sys



with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    k=sum([int(i)**len(test) for i in test])
    if k==int(test):
        print('True')
    else:
        print('False')
