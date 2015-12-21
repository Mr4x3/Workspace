import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    k=dict(zip('abcdefghij',range(10)))
    k.update(dict(zip('0123456789',range(10))))
    l=[]
    for i in test:
        if i in k.keys():
            l.append(i)
        elif i.isdigit():
            l.append(i)
    z=[str(k.get(i)) for i in l]
    print(''.join(z) if z else 'NONE')
