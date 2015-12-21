import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    box, num, happy=[],int(test),1
    while num!=1:
        num=sum([int(i)**2 for i in str(num)])
        if num in box:
            happy=0
            break
        else:
            box.append(num)
    print(happy)
