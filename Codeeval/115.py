import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    t=test.split(',')
    w=[]
    d=[]
    for i in t:
        if i.isalpha():
            w.append(i)
        elif i.isdigit():
            d.append(i)
    if w and d:
        print(','.join(w) + '|' + ','.join(d))
    elif w:
        print(','.join(w))
    elif d:
        print(','.join(d))
