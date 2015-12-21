import sys
    
with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()
x=0
for test in test_cases:
    x=x+int(test)
print(x)
