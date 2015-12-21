import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()


for test in test_cases:
    u=l=0
    t=len(test)
    for k in test:
        if k.isupper():
            u=u+1
        else:
            l+=1
    up=round((u/t)*100,2)
    lp=round((l/t)*100,2)
    print('lowercase: %.2f uppercase: %.2f'%(lp,up))
