import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    sen, num=test.split(';')
    sen=sen.split()
    num=[int(i) for i in num.split()]
    l=list(sen)
    # l=sen.copy() in ver 3.4
    x=0
    last_num=[i for i in range(1,len(sen)+1) if i not in num]
    num.extend(last_num)
    for i in num:
        l[i-1]=sen[x]
        x=x+1
    print(' '.join(l))
