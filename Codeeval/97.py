import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    name, num=test.split('|')
    num=[int(i) for i in num.split()]
    print(''.join([str(name[i-1]) for i in num]))
"""
    l=[]
    for i in num:
        print(name[i-1])

        l.append(name[i-1])
    z=''
    f=1
    for i in l:
        if i.istitle():
            z+=' '+i
        elif i.islower():
            z+=i
        elif i.isdigit() and f:
            z+=' '+i
        else:
            z+=i
    print(z)
"""
