import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    dic={}
    t=test.lower()
    t=''.join(i for i in t if i.isalpha())
    k=set(t)
    for i in k:
        dic[i]=t.count(i)
        lis=sorted(dic.values(), reverse=True)
    m=[]
    x=26
    for j in lis:
        m.append(j*x)
        x=x-1
    print(sum(m))
