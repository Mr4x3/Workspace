# Cool Regex
import sys
import re

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    d,w=test.split()
    regex=re.compile('([a-z]+)(\+|\-)([a-z]+)')
    x,op,z=re.findall(regex,w)[0]
    a,b=int(d[:len(x)]),int(d[len(x):])
    print(a+b if op=='+' else a-b)

# Collapse Code
"""    if w.find('+'):
        x,y,z=w.partition('+')
        print(x,y,z)
    elif w.find('-'):
        x,y,z=w.partition('-') 
    z=dict(zip(i,d))
    a,s='',''
    ck=0
    for i in w:
        while not ck:
            if i.isalpha():
                a=a+i
                break
            else:
                ck=1
                op=i
                break
            break
        s=s+i
    for i in w:
        a=a+z.get(i)
    for i in w:
        s=s+z.get(i)
    if y=='+':
        print(int(a)+int(s))
    else:
        print(int(a)-int(s))
"""
