import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    s=1
    x=''
    for i in test:
        if i.isalpha():
            if s==1:
                x=x+i.capitalize()
                s=0
            else:
                x=x+i.lower()
                s=1
        else:
            x=x+i
    print(x)
                
