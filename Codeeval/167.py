import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    if len(test) <=55:
        print(test)
    else:
        i=40
        for r in range(39,-1,-1):
            if test[r].isspace():
                i=r
                break
            else:
                i=40
            
        k=test[0:i].strip()
        k=k+'... <Read More>'
        print(k)
        
